from django.db import models

# Create your models here.


class House_refer(models.Model):
    class Choices(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4

    Address = models.CharField(max_length=250, blank=False, primary_key=True)
    Bed = models.IntegerField(choices=Choices.choices)
    Bath = models.IntegerField(choices=Choices.choices)
    Storage = models.BooleanField(default=False)
    Wifi = models.BooleanField(default=False)
    Referal_code = models.CharField(
        "enter your friend's referal code if available", max_length=7)


class Refer(models.Model):
    link = models.CharField(max_length=7,  blank=False)
    name = models.CharField(max_length=100, null=False, primary_key=True)
    counter = models.IntegerField(default=0, blank=True)
    Reffered_by = models.CharField(max_length=100)
