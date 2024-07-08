from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()


class Order(models.Model):
    STATUS_CHOICES = (
        ("P", "Pedido realizado"),
        ("F", "Fazendo"),
        ("E", "Saiu para entrega"),
    )
    name_client = models.CharField(max_length=200)
    email_client = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=9)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, max_length=400)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, blank=False, null=False) # noqa
    products = models.ManyToManyField(Product)
