from django.db import models

class Kanon(models.Model):
    kanon_name = models.CharField(max_length=200)
    munition = models.ForeignKey('Munition', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.kanon_name

class User(models.Model):
    user_name = models.CharField(max_length=200)
    kanon = models.ForeignKey(Kanon, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.user_name

class Munition(models.Model):
    amount = models.IntegerField(default=0)
    def __str__(self):
        return str(self.amount)

