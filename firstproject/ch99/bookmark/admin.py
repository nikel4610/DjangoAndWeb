from django.contrib import admin
<<<<<<< HEAD
from firstproject.ch99.bookmark.models import Bookmark

# Register your models here.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')
=======

# Register your models here.
>>>>>>> 337ffff946214b663bcfb929cc76aff8767e11c4
