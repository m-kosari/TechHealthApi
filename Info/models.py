
from django.db import models

# Create your models here.


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=200)
    g_id = models.CharField(max_length=60)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=5)
