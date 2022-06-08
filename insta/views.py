from django.shortcuts import render, redirect
from .models import Image, Profile, Comment, Follow
from .forms import CreateProfileForm, UploadImageForm, FollowForm, UnfollowForm, EditBioForm
from django.http import HttpResponseRedirect, Http404
from .emails import send_signup_email
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = CreateProfileForm()
    return render(request, 'create_profile.html', {"form": form})


# Profile
@login_required(login_url='/accounts/login/')
def profile(request,user_id):
        profile=Profile.objects.get(id=user_id)
        # image = request.user.profile.image.all()
        context = {'profile':profile}
        return render(request, 'profile/profile.html', context)


def profile_edit(request):
    current_user = request.user
    if request.method == "POST":
        form = EditBioForm(request.POST, request.FILES)
        if form.is_valid():
            profile_pic = form.cleaned_data['profile_pic']
            bio  = form.cleaned_data['bio']
            updated_profile = Profile.objects.get(user= current_user)
            updated_profile.profile_pic = profile_pic
            updated_profile.bio = bio
            updated_profile.save()
        return render(request, 'profile.html')
    else:
        form = EditBioForm()
    return render(request, 'edit_profile.html', {"form": form})



# Comment
def comment(request, image_id):
    image = Image.objects.get(pk=image_id)
    content = request.GET.get('comment')
    print(content)
    user = request.user
    comment = Comment( image = image, content = content, user = user)
    comment.save_comment()

    return redirect('home')


# Image Upload
@login_required(login_url='/accounts/login/')
def upload_image(request):
    title = "Instagram | Upload image"
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = profile
            image.save()
        return redirect('home')
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {"form": form, "title": title})


# Like Image
def like_image(request,image_id):
    image = Image.objects.get(pk=image_id)
    liked = False
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    if image.likes.filter(id=profile.id).exists():
        image.likes.remove(profile)
        liked = False
    else:
        image.likes.add(profile)
        liked = True
    return HttpResponseRedirect(reverse('home'))


# Email
@login_required(login_url='/accounts/login/')
def email(request):
    current_user = request.user
    email = current_user.email
    name = current_user.username
    send_signup_email(name, email)
    return redirect(create_profile)



# Home
@login_required(login_url='/accounts/login/')
def home(request):
    title= "Instagram"
    current_user =request.user
    try:
        logged_in = Profile.objects.get(user = current_user)
    except Profile.DoesNotExist:
        raise Http404()

    timeline_images = []
    current_images = Image.objects.filter(profile = logged_in)
    for current_image in current_images:
        timeline_images.append(current_image.id)

    current_following = Follow.objects.filter(follower = logged_in)
    for following in current_following:
        following_profile = following.followed
        following_images = Image.get_profile_images(following_profile)
        for image in following_images:
            timeline_images.append(image.id)

    display_images= Image.objects.filter(pk__in = timeline_images).order_by('-post_date')
    liked = False
    for i in display_images:
        image = Image.objects.get(pk=i.id)
        liked = False
        if image.likes.filter(id =request.user.id).exists():
            liked = True
    comments = Comment.objects.all()[:3]
    comments_count= comments.count()

    suggestions = Profile.objects.all()[:4]
    print("SUGGESTED")
    print(suggestions[0])
    return render(request, 'home.html', {"images":display_images,"liked":liked, "comments":comments, "title":title, "suggestions":suggestions, "loggedIn":logged_in})

# Profile Search
def search_profile(request):
    if 'search_user' in request.GET and request.GET['search_user']:
        name = request.GET.get("search_user")
        results = Profile.search_profile(name)
        print(results)
        message = f'name'
        context = {
            'results': results,
            'message': message
        }
        return render(request, 'search.html', context)
    else:
        message = "No username was found !"
    return render(request, 'search.html', {'message': message})


