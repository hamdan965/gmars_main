from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    link = models.URLField(max_length=500)

    def __str__(self):
        return self.name





