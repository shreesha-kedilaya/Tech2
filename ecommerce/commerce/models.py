from django.db import models
from polymorphic.models import PolymorphicModel

# Create your models here.

class PersonalInfo(models.Model):

    address = models.CharField(max_length=250)
    country = models.CharField(max_length=15)
    phoneNumber = models.CharField(max_length=15)
    postalCode = models.CharField(max_length=10)

class User(PolymorphicModel):
    
    contactName = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=500)

    personalInfo = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.contactName + self.email


class Product(models.Model):

    supplier = models.ForeignKey(User, on_delete=models.CASCADE)

    productName = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()

class Cart(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE)

    products = models.ManyToManyField(Product)

class Admin(User):
    pass

class Company(PolymorphicModel):
    personalInfo = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE)

class Shipper(Company):
    pass

class Order(models.Model):

    orderNumber = models.PositiveIntegerField()
    orderDate = models.DateTimeField()
    deliveryDate = models.DateTimeField()
    shippedDate = models.DateTimeField()
    shipper = models.ForeignKey(Shipper, on_delete=models.DO_NOTHING)

    user = models.OneToOneField(User, on_delete=models.CASCADE)


class BillingInfo(models.Model):

    billingAddress = models.CharField(max_length=250)
    creditCard = models.PositiveIntegerField()
    billDate = models.DateTimeField()
    creditCardPin = models.PositiveSmallIntegerField()