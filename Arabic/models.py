from django.db import models

# Create your models here.


class TransModel(models.Model):
    title = models.CharField(max_length=127)
    info = models.TextField()