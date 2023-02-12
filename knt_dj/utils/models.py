from django.db import models


class Color(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Size(models.Model):
    unit = models.CharField(max_length=10)

    def __str__(self):
        return self.unit


class State(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.RESTRICT, related_name='city')
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
