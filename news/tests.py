from django.test import TestCase
from django.contrib.auth.models import User
from .models import Topic, Content, Comment
from django.utils.text import slugify

class ModelsTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass1234')
        self.topic = Topic.objects.create(name='Django')
        self.content = Content.objects.create(
            title='Test Content',
            author=self.user,
            slug=slugify('Test Content'),
            body='This is a test content body.',
        )
        self.content.topics.add(self.topic)

    def test_topic_str(self):
        self.assertEqual(str(self.topic), 'Django')

    def test_content_str(self):
        self.assertEqual(str(self.content), 'Test Content')

    def test_content_creation(self):
        self.assertEqual(self.content.author, self.user)
        self.assertEqual(self.content.body, 'This is a test content body.')
        self.assertIn(self.topic, self.content.topics.all())

    def test_content_likes(self):
        self.content.likes.add(self.user)
        self.assertIn(self.user, self.content.likes.all())

    def test_comment_str_and_is_replied(self):
        comment = Comment.objects.create(
            content=self.content,
            author=self.user,
            body='Top level comment'
        )
        self.assertEqual(str(comment), 'Top level comment')
        self.assertFalse(comment.is_replied())

        reply = Comment.objects.create(
            content=self.content,
            author=self.user,
            body='Reply comment',
            parent=comment
        )
        self.assertTrue(reply.is_replied())

    def test_comment_likes(self):
        comment = Comment.objects.create(
            content=self.content,
            author=self.user,
            body='Comment with likes'
        )
        comment.likes.add(self.user)
        self.assertIn(self.user, comment.likes.all())
