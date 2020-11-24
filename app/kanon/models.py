from django.db import models

class Kanon(models.Model):
    kanon_name = models.CharField(max_length=200)

    def __str__(self):
        return self.kanon_name

class User(models.Model):
    user_name = models.CharField(max_length=200)
    kanon = models.ForeignKey(Kanon, on_delete=models.CASCADE)
    def __str__(self):
        return self.user_name

class Munition(models.Model):
    amount = models.IntegerField(default=0)
    kanon = models.ForeignKey(Kanon, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.amount)

