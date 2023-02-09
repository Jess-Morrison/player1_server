from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
    about_me = models.CharField(max_length=250)
    user_name = models.CharField(max_length=250)
    tag_line = models.CharField(max_length=50)
    image_url = models.CharField(max_length=200)
