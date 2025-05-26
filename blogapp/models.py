from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.date_added}'
