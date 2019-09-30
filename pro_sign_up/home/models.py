from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=500000)
    very     = models.CharField(max_length=500000)
    link     = models.CharField(max_length=500000)

    def __str__(self):
        return self.username

