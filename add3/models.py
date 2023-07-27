from django.db import models


class News(models.Model):
    title = models.CharField(max_length=40)
    body = models.TextField()
    img = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title

