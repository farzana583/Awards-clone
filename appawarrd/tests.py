from django.test import TestCase
from .models import Image, Profile
from django.contrib.auth.models import User

# Create your tests here.
class TestImage(TestCase):
    def setUp(self):
        self.user = User(username='Farzana')
        # self.user.save()
        self.post_test = Post(title=title, user_name='Farzana', inage='default.jpg', project='pizza shop')

    def test_instance(self):
        self.assertTrue(isinstance(self.post_test, Post))
        
    def test_save_post(self):
        posts = Post.objects.all()

    def test_delete_post(self):
        before = Profile.objects.all()
        after = Profile.objects.all()
        self.assertTrue(len(before) == len(after))


# class TestProfile(TestCase):
#     def setUp(self):
#         self.user = User(username='Farzana')
#         self.user.save()
#         self.profile_test = Profile(user=self.user, image='default.jpg', bio='this is my website' )

    def test_instance(self):
        self.assertTrue(isinstance(self.profile_test, Profile))