from django.db import models

#test

class User(models.Model):
    user_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name

class Munition(models.Model):
    amount = models.IntegerField(default=0)

    def __str__(self):
        return self.amount

class Kanon(models.Model):
    kanon_name = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    munition = models.ForeignKey(Munition, on_delete=models.CASCADE)

    def __str__(self):
        return self.kanon_name

