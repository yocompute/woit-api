from django.db import models
from django.db.models import CharField, Model, ForeignKey, DateTimeField, DecimalField
from django.contrib.auth.models import User
from items.models import Product

Status = (('completed','Completed'), ('pending', 'Pending'))
CURRENCIES = (('usd','USD'), ('cad', 'CAD'), ('cny','CNY'))

class Order(Model):
    price = DecimalField(max_digits=10, decimal_places=3, null=True)
    currency = CharField(max_length=16, choices=CURRENCIES, default='usd') 
    discount = DecimalField(max_digits=10, decimal_places=3, null=True) 
    tax = DecimalField(max_digits=10, decimal_places=3, null=True) 
    total = DecimalField(max_digits=10, decimal_places=3, null=True) 
    status = CharField(max_length=32, choices=Status, default='pending')
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    product = ForeignKey(Product, null=True, blank=True)
    buyer = ForeignKey(User, null=True, blank=True)
