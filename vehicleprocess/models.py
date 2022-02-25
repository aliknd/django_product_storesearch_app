from django.db import models

# Create your models here.

class Car(models.Model):
    model_year = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    rejection_percentage = models.CharField(max_length=100)
    reason_1 = models.TextField()
    reason_2 = models.TextField()
    reason_3 = models.TextField()

    def __str__(self):
        return self.model