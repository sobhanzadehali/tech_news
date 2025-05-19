from django.core.management.base import BaseCommand
from news.models import Content, Topic, Comment
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from django.utils.text import slugify
from django.utils.dateparse import parse_datetime  # Optional
import time
import datetime

class Command(BaseCommand):
    help = 'Scrapes a website using Selenium'

    def handle(self, *args, **options):
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium"
        chrome_options.add_argument('--headless')  # Run headless
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--window-size=1920x1080')

        driver = webdriver.Chrome(options=chrome_options)

        try:
            driver.get('https://www.zoomit.ir/')
            time.sleep(3)

            articles = driver.find_elements(By.XPATH, '//div[@class="mt-4 flex flex-col gap-4 px-4 md:gap-4 xl:px-0"]/a')
            post_links = [elem.get_attribute("href") for elem in articles if elem.get_attribute("href")]

            for post_link in post_links:
                driver.get(post_link)
                time.sleep(2)

                try:
                    author = driver.find_element(By.XPATH, '//div[@class="sc-a11b1542-0 GGjpx"]//span').text.strip()
                    title = driver.find_element(By.XPATH, '//h1').text.strip()
                    created_date_raw = driver.find_element(By.XPATH, '//span[@class="sc-9996cfc-0 inKOvi fa"]').text.strip()


                    topic_elements = driver.find_elements(By.XPATH, '//div[@class="sc-a11b1542-0 fCUOzW"]//span')
                    topics = [el.text.strip() for el in topic_elements]

                    comment_elements = driver.find_elements(By.XPATH, '//div[@class="sc-a11b1542-0 gjkguG"]//div[@class="sc-a11b1542-0 irBfRc w-full"]//span')
                    comments = [el.text.strip() for el in comment_elements]

                    likes = driver.find_element(By.XPATH, '//button[@class="sc-9bfa8572-0 jbTKNm sc-da2a67e0-2 fbrNkT"]//span').text.strip()

                    body_parts = driver.find_elements(By.XPATH, '//p[@class="sc-9996cfc-0 gAFslo sc-b2ef6c17-0 joXpaW"]')
                    body = ''.join([bp.get_attribute("innerHTML").strip() for bp in body_parts])

                    # Save topics
                    topic_objs = []
                    for name in topics:
                        if name:
                            t, _ = Topic.objects.get_or_create(name=name)
                            topic_objs.append(t)
                    print(topic_objs)
                    # Save content
                    content_obj, _ = Content.objects.update_or_create(
                        title=title,
                        defaults={
                            'slug': slugify(title),
                            'author': author,
                            'body': body,
                            'created_at': created_date_raw,
                        }
                    )
                    content_obj.topics.set(topic_objs)
                    

                    # Save comments
                    for comment_text in comments:
                        if comment_text:
                            Comment.objects.update_or_create(
                                content=content_obj,
                                body=comment_text,
                                defaults={
                                    'author': 'Anonymous',
                                    'created_at': created_date_raw
                                }
                            )

                    print(f"✅ Saved content: {title}")

                except Exception as e:
                    print(f"❌ Error processing post {post_link}: {e}")

        except Exception as e:
            print(f"❌ Error opening Zoomit: {e}")
        finally:
            driver.quit()
