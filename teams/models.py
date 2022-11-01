from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=40)
    federation = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    fundation_date = models.DateField()

    def  __str__(self):
        return f"{self.name} - {self.country}"