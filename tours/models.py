from django.db import models

class TourPackage(models.Model):
    CATEGORY_CHOICES = [
        ('International', 'International Tour'),
        ('Universe', 'Universe Tour'),
        ('Family', 'Family Tour'),
    ]
    
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    places = models.TextField()
    combo_available = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, default="Available")

    def __str__(self):
        return self.name

class Booking(models.Model):
    package = models.ForeignKey(TourPackage, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.package.name}"

# Create your models here.
