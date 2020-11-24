from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=200)

class Munition(models.Model):
    amount = models.IntegerField(default=0)

class Kanon(models.Model):
    kanon_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    munition = models.ForeignKey(Munition, on_delete=models.CASCADE)

