from django.db import models
from django.db.models import CharField, Model, ForeignKey, DateTimeField, DecimalField
from django.contrib.auth.models import User
from items.models import Product

Status = (('accepted','Accepted'), ('pending', 'Pending'), ('expired', 'Expired'), ('accepted expiry', 'Accepted Expiry'))
CURRENCIES = (('usd','USD'), ('cad', 'CAD'), ('cny','CNY'))

class Transaction(Model):
    price = DecimalField(max_digits=10, decimal_places=3, null=True)
    currency = CharField(max_length=16, choices=CURRENCIES, default='usd') 
    tax = DecimalField(max_digits=10, decimal_places=3, null=True) 
    total = DecimalField(max_digits=10, decimal_places=3, null=True)
    status = CharField(max_length=32, choices=Status, default='pending')
    created = DateTimeField(auto_now_add=True)
    
    product = ForeignKey(Product, null=True, blank=True)
    buyer = ForeignKey(User, null=True, blank=True)

class Bid(Model):
    start_price = DecimalField(max_digits=10, decimal_places=3, null=True) 
    expect_price = DecimalField(max_digits=10, decimal_places=3, null=True) # For auto deal and buyout
    currency = CharField(max_length=16, choices=CURRENCIES, default='usd')
    status = CharField(max_length=32, choices=Status, default='pending')
    created = DateTimeField(auto_now_add=True)
    expiry = DateTimeField(auto_now_add=True)

    product = ForeignKey(Product, null=True, blank=True)
    accepted_bid = ForeignKey(Transaction, null=True)
