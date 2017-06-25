from django.db import models
from django.db.models import CharField, Model, ForeignKey, DateTimeField, DecimalField
from django.contrib.auth.models import User
from items.models import Item

Status = (('completed','Completed'), ('pending', 'Pending'))

class Order(Model):
    price = DecimalField(max_digits=10, decimal_places=3, null=True) 
    discount = DecimalField(max_digits=10, decimal_places=3, null=True) 
    tax = DecimalField(max_digits=10, decimal_places=3, null=True) 
    total = DecimalField(max_digits=10, decimal_places=3, null=True) 
    status = CharField(max_length=32, choices=Status, default='pending')
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    item = ForeignKey(Item)
    buyer = ForeignKey(User)
