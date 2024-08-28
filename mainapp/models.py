from django.db import models


class Titanic(models.Model):
    passengerID = models.IntegerField(null=True, blank=True, unique=True)

    SURVIVED_CHOICES = [
        (0, 'Died'),
        (1, 'Survived'),
    ]
    survived = models.IntegerField(choices=SURVIVED_CHOICES, null=True, blank=True)

    PCLASS_CHOICES = [
        (1, 'First Class'),
        (2, 'Second Class'),
        (3, 'Third Class'),
    ]

    pclass = models.IntegerField(choices=PCLASS_CHOICES, null=True, blank=True)
    name = models.CharField(blank=True)

    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    sex = models.CharField(choices=SEX_CHOICES, blank=True)
    age = models.FloatField(null=True, blank=True)
    sibsp = models.IntegerField(null=True, blank=True)
    parch = models.IntegerField(null=True, blank=True)
    ticket = models.CharField(blank=True)
    fare = models.FloatField(null=True, blank=True)
    cabin = models.CharField(blank=True)

    EMBARKED_CHOICES = [
        ('C', 'Cherbourg'),
        ('S', 'Southampton'),
        ('Q', 'Queenstown'),
    ]
    embarked = models.CharField(choices=EMBARKED_CHOICES, blank=True)

    def __str__(self):
        return self.name
