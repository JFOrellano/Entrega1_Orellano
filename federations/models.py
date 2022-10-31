from django.db import models

# Create your models here.
class Federation(models.Model):
    name = models.CharField(max_length=40)
    initials = models.CharField(max_length=40)
    official_website = models.CharField(max_length=40)

    def  __str__(self):
        return f"{self.initials} - {self.name}"