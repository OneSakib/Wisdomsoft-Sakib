from django.db import models


# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)

    def __str__(self):
        return self.name
