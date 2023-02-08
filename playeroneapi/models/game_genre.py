from django.db import models

class GameGenre(models.Model):
  game_genre_name = models.CharField(max_length=50) 
