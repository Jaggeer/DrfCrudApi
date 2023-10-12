from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.ForeignKey('Price', on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField()
    barcode = models.PositiveIntegerField()
    updateDate = models.DateField(auto_now=True)
    productType = models.ForeignKey('ProductType', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title

class ProductType(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField()

    def __str__(self):
        return self.title

class Price(models.Model):
    currency = models.CharField(max_length=1)
    price = models.FloatField()

    def __str__(self):
        return self.currency + str(self.price)