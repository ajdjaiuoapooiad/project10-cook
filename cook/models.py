from django.db import models
from django.utils import timezone

class Post(models.Model):
    title=models.CharField('タイトル',max_length=20)
    text=models.TextField('本文')
    created_at=models.DateTimeField('日付',default=timezone.now)
    
    def __str__(self):
        return self.title[:10]