from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    name = models.CharField(max_length=80, blank=True)
    profile_pic = CloudinaryField('image')
    bio =  models.TextField(blank=True)
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()

    @receiver(post_save,sender=User)
    def createUserProfile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
            
    @receiver(post_save,sender=User)
    def saveUserProfile(sender, instance, **kwargs):
        instance.profile.save()
    def saveProfile(self):
        self.user()


