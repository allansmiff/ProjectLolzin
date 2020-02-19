from django.db import models


# Create your models here.
class Summoner(models.Model):
    id = models.CharField
    accountId = models.CharField
    puuid = models.CharField
    name = models.CharField
    profileIconId = models.IntegerField
    revisionDate = models.BigIntegerField
    summonerLevel = models.IntegerField
