# Создайте три модели Django: клиент, товар и заказ.

# Клиент может иметь несколько заказов. Заказ может содержать несколько товаров. Товар может входить в несколько заказов.

# Поля модели «Клиент»:
# — имя клиента
# — электронная почта клиента
# — номер телефона клиента
# — адрес клиента
# — дата регистрации клиента

# Поля модели «Товар»:
# — название товара
# — описание товара
# — цена товара
# — количество товара
# — дата добавления товара

# Поля модели «Заказ»:
# — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
# — связь с моделью «Товар», указывает на товары, входящие в заказ
# — общая сумма заказа
# — дата оформления заказа

# Допишите несколько функций CRUD для работы с моделями по желанию. Что по вашему мнению актуально в такой базе

from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    adress = models.CharField(max_length=200)
    register_date = models.DateField(auto_now=True)

    def __str__(self):
        return f'{self.name} {self.register_date}'
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.IntegerField()
    date_income = models.DateField(auto_now=True)


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateField(auto_now=True)
