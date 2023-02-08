from django.db import models

class VideoGame(models.Model):
  user = models.ForeignKey("User", on_delete=models.CASCADE)
  game_title = models.CharField(max_length=50)
  game_genre = models.CharField(max_length=50)
  purchase_location = models.CharField(max_length=50)
  game_format = models.CharField(max_length=50)
  description = models.CharField(max_length=50)
  imageURL = models.CharField(max_length=50)
