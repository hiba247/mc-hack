from django.db import models

class etat(models.Model):
    mounth = models.IntegerField()
    year = models.IntegerField()
    pressure = models.FloatField()
    temperateur = models.FloatField()
    flow = models.FloatField()
    level = models.FloatField()
    gas = models.FloatField()
    vibration = models.FloatField()

class solution(models.Model):
    solu=models.TextField()
    prblm = models.IntegerField()

class percontage(models.Model):
    pressure = models.FloatField()
    temperateur = models.FloatField()
    flow = models.FloatField()
    level = models.FloatField()
    gas = models.FloatField()
    vibration = models.FloatField()