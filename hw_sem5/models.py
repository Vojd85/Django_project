from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    adress = models.CharField(max_length=200)
    register_date = models.DateField(auto_now=True)
    birthday = models.DateField(default=None)

    def __str__(self):
        return f'{self.name} {self.register_date}'
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    date_income = models.DateField(auto_now=True)
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name



class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now=True)