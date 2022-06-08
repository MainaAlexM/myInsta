from django.test import TestCase
from django.contrib.auth.models import User
from .models import Image, Profile, Comment, Follow

# Model Classes Tests

# Image
class ImageTestClass(TestCase):
    def setUp(self):
        self.apptester = User(username = "apptester", email = "apptestermind@gmail.com",password = "Tester@1234")
        self.profile = Profile(bio='bio', user= self.apptester)
        self.rider = Image(image = 'my_image', name ='rider', caption = 'dream of a bike', profile = self.profile)
        self.foods = Image(image = 'my_image', name ='foods', caption = 'Eat as You Please', profile = self.profile)

        self.apptester.save()
        self.profile.save()
        self.rider.save_image()

    def tearDown(self):
        Image.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.rider, Image))

    def test_save_image_method(self):
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)

    def test_delete_image(self):
        images1 = Image.objects.all()
        self.assertEqual(len(images1),1)
        self.rider.delete_image()
        images2 = Image.objects.all()
        self.assertEqual(len(images2),0)

    def test_update_caption(self):
        self.rider.update_caption('dream of a bike')
        self.assertEqual(self.rider.caption, 'dream of a bike')

    def test_get_profile_images(self):
        self.foods.save_image()
        images = Image.get_profile_images(self.profile)
        self.assertEqual(len(images),2)


#Profile
class ProfileTestClass(TestCase):
    def setUp(self):
        self.apptester = User(username = 'apptester', email = 'apptestermind@gmail.com', password = 'Tester@1234')
        self.profile = Profile(bio = 'info', user = self.apptester)
        self.apptester.save()

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.apptester, User))
        self.assertTrue(isinstance(self.profile, Profile))

    def test_search_user(self):
        user = Profile.search_user(self.apptester)
        self.assertEqual(len(user), 1)


# Comment
class CommentTestClass(TestCase):
    def setUp(self):
        self.apptester = User(username = "apptester", email = "apptestermind@gmail.com",password = "Tester@1234")
        self.profile = Profile(bio='bio', user= self.apptester)
        self.rider = Image(image = 'my_image', name ='rider', caption = 'Riding never gets old', profile = self.profile)
        self.comment = Comment(image=self.rider, content= 'dream of a bike', user = self.apptester)

        self.apptester.save()
        self.profile.save()
        self.rider.save_image()
        self.comment.save_comment()

    def tearDown(self):
        Image.objects.all().delete()
        Comment.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        comments = Comment.objects.all()
        self.assertTrue(len(comments)> 0)

    def test_delete_comment(self):
        comments1 = Comment.objects.all()
        self.assertEqual(len(comments1),1)
        self.comment.delete_comment()
        comments2 = Comment.objects.all()
        self.assertEqual(len(comments2),0)

    def test_get_image_comments(self):
        comments = Comment.get_image_comments(self.rider)
        self.assertEqual(comments[0].content, 'dream of a bike')
        self.assertTrue(len(comments) > 0)

# Follow
class FollowTestClass(TestCase):
    def setUp(self):
        self.apptester = User(username = 'apptester', email = 'apptestermind@gmail.com', password = 'Tester@1234')
        self.profile1 = Profile(bio = 'bio', user = self.apptester)
        self.person1 = User(username = 'person1', email = 'apptestermind@gmail.com', password = '12345')
        self.profile2 = Profile(bio = 'bio', user = self.person1)
        self.apptester.save()
        self.person1.save()
        self.follow = Follow  (followed = self.profile1, follower = self.profile2)

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.follow,Follow))