from django.db import models

# Create your models here.
class Player(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    mail = models.CharField(max_length=40)
    password = models.IntegerField()
    

    def  __str__(self):
        return f"{self.name} - {self.last_name} - {self.number}"