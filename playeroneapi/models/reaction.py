from django.db import models


class Reaction(models.Model):
    reaction_name = models.CharField(max_length=50)
    image_url = models.CharField(max_length=50)
    
    def __init__(self, *args, **kwargs):
        super(Reaction, self).__init__(*args, **kwargs)
        self.__clicked = False
        self.__count = 0

    @property
    def clicked(self):
        return self.__clicked

    @clicked.setter
    def clicked(self, bool):
        self.__clicked = bool

    @property
    def count(self):
        return self.__count

    @count.setter
    def count(self, value):
        self.__count = value
