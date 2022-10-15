from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class GunsModel(models.Model):
    name=models.CharField(max_length=50)
    quality=models.CharField(max_length=50)
    discription=models.TextField(max_length=50)
    price=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10000)])
    def __str__(self):
        return f"{ self.name}"