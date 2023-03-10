from django.db import models
from django.urls import reverse


class Days(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('day', kwargs={'pk': self.pk})


class Post(models.Model):
    day = models.ForeignKey(Days,on_delete=models.CASCADE)
    text = models.CharField(max_length=400)

    def __str__(self):
        return self.text

