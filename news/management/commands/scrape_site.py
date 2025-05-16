from django.core.management.base import BaseCommand
from news.models import Content, Topic, Comment
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


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
            articles = driver.find_elements(By.XPATH,
                                            '//div[@class="mt-4 flex flex-col gap-4 px-4 md:gap-4 xl:px-0"]/a')
            post_links = [elem.get_attribute("href") for elem in articles]
            for post_link in post_links:
                driver.get(post_link)
                time.sleep(2)
                author = driver.find_element(By.XPATH, '//div[@class="sc-a11b1542-0 GGjpx"]//span').text
                title = driver.find_element(By.XPATH, '//h1').text
                topic_elements = driver.find_elements(By.XPATH, '//div[@class="sc-a11b1542-0 fghZoF"]//a')
                topics = [el.text for el in topic_elements]
                created_date = driver.find_element(By.XPATH, '//span[@class="sc-9996cfc-0 inKOvi fa"]')
                comment_elements = driver.find_elements(By.XPATH,
                                                        '//div[@class="sc-a11b1542-0 gjkguG"]//div[@class="sc-a11b1542-0 irBfRc w-full"]')
                comments = [el.text for el in comment_elements]
                likes = driver.find_element(By.XPATH,
                                            '//button[@class="sc-9bfa8572-0 jbTKNm sc-da2a67e0-2 fbrNkT"]//span').text
                body_parts = driver.find_elements(By.XPATH, '//p[@class="sc-9996cfc-0 gAFslo sc-b2ef6c17-0 joXpaW"]')
                body = ''
                for body_part in body_parts:
                    body += body_part.get_attribute("innerHTML")
                post = {
                    'title': title,
                    'author': author,
                    'topics': topics,
                    'created_date': created_date.text,
                    'comments': comments,
                    'likes': likes,
                    'body': body,
                }
                for i in post['topics']:
                    ts = Topic.objects.update_or_create(name=i)
                cn, created_obj = Content.objects.update_or_create(title=post['title'],
                                                                   author=post['author'],
                                                                   body=post['body'],
                                                                   created_at=post['created_date'],
                                                                   )
                for comment in post['comments']:
                    Comment.objects.update_or_create(content=cn, body=comment)
                self.stdout.write(self.style.SUCCESS('Successfully updated content'))

        finally:
            driver.quit()
