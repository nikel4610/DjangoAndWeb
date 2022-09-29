"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mysite import views
from mysite.views import *
from bookmark.views import BookmarkLV, BookmarkDV

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

from django.conf.urls.static import static
from django.conf import settings

from post.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('bookmark/', BookmarkLV.as_view(), name='index'),
    # path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),

    path('', HomeView.as_view(),  name='home'),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('photo/', include('photo.urls')),
    path('post/', include('post.urls')),
    path('post/<int:pk>/', posting, name='posting'),
    path('post/new_post/', new_post, name='new_post'),
    path('post/<int:pk>/remove/', remove_post),

    # path('bookmark/', ListView.as_view(model=Bookmark), name='index'),
    # path('bookmark/<int:pk>/', DetailView.as_view(model=Bookmark), name='detail'),

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', views.UserCreateDoneTV.as_view(), name='register_done'),

    path('space', views.SpaceAPI_FV, name='space'),

    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
