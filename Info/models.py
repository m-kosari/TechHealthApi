from django.db import models


# Create your models here.


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.CharField(max_length=200)
    g_id = models.CharField(max_length=60)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=5)


class UserInfo(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id_user = models.IntegerField()
    dev_id = models.CharField(max_length=200)
    dev_name = models.CharField(max_length=120)
    dev_model = models.CharField(max_length=120)


class Package(models.Model):
    id = models.AutoField(primary_key=True)
    pck = models.CharField(max_length=200)
    label = models.CharField(max_length=50)
    sts = models.CharField(max_length=4)


class Statuses(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id_user = models.IntegerField()
    pck = models.CharField(max_length=200)
    date = models.CharField(max_length=15)
    long = models.BigIntegerField()


class GuestStatuses(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    dev_id = models.CharField(max_length=200)
    pck = models.CharField(max_length=200)
    date = models.CharField(max_length=15)
    long = models.BigIntegerField()


class Reports(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.IntegerField()
    report = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
