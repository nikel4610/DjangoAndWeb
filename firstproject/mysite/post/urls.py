from django.urls import path, re_path
from .views import *

app_name = 'post'

urlpatterns = [
    path('', index, name='index'),
    path('post/', post, name='post'),
    path('post/new_post/', new_post),
]