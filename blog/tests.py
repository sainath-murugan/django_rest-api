from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post
# Create your tests here.

class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        create_user = User.objects.create_user(
            username="test_user",
            password="12345"
        )
        create_user.save()

        create_post = Post.objects.create(
            author=create_user,
            title="a",
            body="b"
        )
        create_post.save()
    
    def test_content(self):
        post = Post.objects.get(id=1)
        author = post.author
        title = post.title
        body = post.body
        self.assertEqual(str(author), "test_user")
        self.assertEqual(str(title), "a")
        self.assertEqual(str(body), "b")

