from django.db import models
from accounts.models import User, TimeStampedModel
# Create your models here.
class Property(TimeStampedModel):
    PROPERTY_TYPE = [
        ('apartment', 'APARTMENT'),
        ('house', 'HOUSE'),
        ('pg', 'PG')
    ]

    STATUS = [
        ('available', 'AVAILABLE'),
        ('rented', 'RENTED'),
        ('sold', 'SOLD'),
    ]
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    property_type = models.CharField(choices=PROPERTY_TYPE)
    title = models.CharField(max_length=128, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.CharField(max_length=8, blank=False)
    address = models.TextField(blank=False)
    city= models.CharField(max_length=50, blank=False)
    state = models.CharField(max_length=50, blank=False)
    zipcode = models.CharField(max_length=20, blank=False)
    status = models.CharField( max_length=50, choices=STATUS)

    class Meta:
        def __str__(self):
            return self.title
    
class 