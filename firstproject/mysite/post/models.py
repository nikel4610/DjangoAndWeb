from email.policy import default
from django.db import models

# Create your models here.
class post(models.Model):
    postname = models.CharField(max_length=50, blank=True, null=True)
    # 게시글 Post에 이미지 추가
    mainphoto = models.ImageField(blank=True, null=True)
    contents = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.postname