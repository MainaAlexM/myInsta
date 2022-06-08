from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('search/',views.search_profile,name ='search'),
    path('email/',views.email,name='email'),
    path('create_profile/',views.create_profile,name = 'create_profile'),
    path('profile/edit', views.profile_edit,name = 'profile_edit'),
    path('profile/<user_id>',views.profile,name = 'profile'),
    path('upload/image', views.upload_image, name = "upload_image"),
    path('comment/(<image_id>\d+)', views.comment,name = "comment"),
    path('like/(<image_id>\d+)', views.like_image, name = 'like_image'),
]