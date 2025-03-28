from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='destinations/')
    

    def __str__(self):
        return self.name

