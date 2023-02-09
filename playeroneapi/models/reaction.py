from django.db import models

class Reaction(models.Model):
  reaction_name = models.CharField(max_length=50)
  image_url = models.CharField(max_length=50)
