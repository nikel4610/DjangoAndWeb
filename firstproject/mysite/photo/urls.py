from django.urls import path
from photo import views

app_name = 'photo'
urlpatterns = [
    # example: /photo/
    path('', views.AlbumLV.as_view(), name='index'),

    # exapmle: photo/album/, same as /photo/
    path('album', views.AlbumLV.as_view(), name='album_list'),

    # example: /photo/album/99/
    path('album/<int:pk>/', views.AlbumDV.as_view(), name='album_detail'),

    # example: /photo/photo/99/
    path('photo/<int:pk>/', views.PhotoDV.as_view(), name='photo_detail'),
]