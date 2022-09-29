from django.contrib import admin
from post.models import post

# Register your models here.
@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display = ('postname', 'contents', 'mainphoto')
