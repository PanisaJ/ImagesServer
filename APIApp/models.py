from django.db import models

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=40)
    def __str__(self):
        return self.username

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default='')
    photo = models.ImageField(blank=False,null=False)
    caption = models.TextField(null=True)
    def __str__(self):
        return self.photo.name

class Comment(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE,default='')
    comment_text = models.CharField(max_length=200,default='')
    def __str__(self):
        return self.comment_text



