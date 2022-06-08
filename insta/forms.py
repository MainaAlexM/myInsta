from django.forms import ModelForm
from .models import Profile, Follow, Image

class CreateProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['created', 'account_holder', 'followers', 'following']


class EditBioForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class UploadImageForm(ModelForm):
    class Meta :
        model = Image
        exclude = ['profile', 'post_date', 'likes']


class FollowForm(ModelForm):
    class Meta:
        model = Follow
        exclude = ['followed', 'follower']


class UnfollowForm(ModelForm):
    class Meta:
        model = Follow
        exclude = ['followed', 'follower']

