from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.TextField()
    game_dir = models.TextField()
