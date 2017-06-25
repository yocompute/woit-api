from django.db import models
from django.db.models import CharField, Model, ForeignKey, DateTimeField, DecimalField
from django.contrib.auth.models import User
from items.models import Item

Status = (('accepted','Accepted'), ('pending', 'Pending'), ('expired', 'Expired'), ('accepted expiry', 'Accepted Expiry'))

class Transaction(Model):
    price = DecimalField(max_digits=10, decimal_places=3, null=True) 
    tax = DecimalField(max_digits=10, decimal_places=3, null=True) 
    total = DecimalField(max_digits=10, decimal_places=3, null=True)
    status = CharField(max_length=32, choices=Status, default='pending')
    created = DateTimeField(auto_now_add=True)
    
    item = ForeignKey(Item)
    buyer = ForeignKey(User)

class Bid(Model):
    start_price = DecimalField(max_digits=10, decimal_places=3, null=True) 
    expect_price = DecimalField(max_digits=10, decimal_places=3, null=True) # For auto deal
    status = CharField(max_length=32, choices=Status, default='pending')
    created = DateTimeField(auto_now_add=True)
    expiry = DateTimeField(auto_now_add=True)

    item = ForeignKey(Item)
    accepted_bid = ForeignKey(Transaction, null=True)