from django.db import models

# Create your models here.
class Post (models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return str(self.title)

class ImageUpload(models.Model):
    pic = models.FileField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title