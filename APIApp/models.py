from django.db import models

class Image(models.Model):
    username = models.CharField(max_length=200,default='')
    photo = models.ImageField(blank=False,null=False)
    caption = models.TextField(null=True)
    def __str__(self):
        return self.photo.name

class Comment(models.Model):
    photoID = models.IntegerField(default=0)
    comment_text = models.CharField(max_length=200,default='')
    def __str__(self):
        return self.comment_text
