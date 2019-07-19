from django.db import models

# Create your models here.


class BaseUrl(models.Model):
    url = models.CharField(max_length=200)


class PageUrl(models.Model):
    page = models.CharField(max_length=200)


class SubPage(models.Model):
    sub_page = models.CharField(max_length=200)


class BaseUrlImages(models.Model):
    home_image = models.CharField(max_length=200)


class PageImages(models.Model):
    page_image = models.CharField(max_length=200)

class UrlDepth(models.Model):
    url=models.CharField(max_length=200)
    depth=models.IntegerField(max_length=10)

