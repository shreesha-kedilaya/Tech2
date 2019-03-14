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

    personalInfo = models.OneToOneField(PersonalInfo, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.contactName + self.email


class Session(models.Model):

    sessionId = models.UUIDField(unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

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

class OrderDetails(models.Model):

    product = models.OneToOneField(Product, on_delete=models.DO_NOTHING)
    unitPrice = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()

class Order(models.Model):

    orderNumber = models.PositiveIntegerField()
    orderDate = models.DateTimeField()
    deliveryDate = models.DateTimeField()
    shippedDate = models.DateTimeField()
    shipper = models.ForeignKey(Shipper, on_delete=models.DO_NOTHING)

    orderDetails = models.OneToOneField(OrderDetails, on_delete=models.DO_NOTHING)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class BillingInfo(models.Model):

    billingAddress = models.CharField(max_length=250)
    creditCard = models.PositiveIntegerField()
    billDate = models.DateTimeField()
    creditCardPin = models.PositiveSmallIntegerField()

class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)