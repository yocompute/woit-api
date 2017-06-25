from django.contrib.auth.models import User
from django import forms
from django.db import models
from django.db.models import CharField, Model, ForeignKey, DateTimeField, DecimalField

TYPES = (('photo','Photo'), ('paint', 'Paint'))
SOURCES = (('original','Original'), ('market', 'From Market'))
CURRENCIES = (('usd','USD'), ('cad', 'CAD'), ('cny','CNY'))
STYLES = (('contemporary', 'Contemporary'), ('modern', 'Modern'))
STATUS = (('active','Active'), ('inactive', 'Inactive'))

class Item(Model):
    title = CharField(max_length=255, null=True, blank=True)
    description = CharField(max_length=1000, null=True, blank=True)
    dimension = CharField(max_length=255, null=True, blank=True)
    author = CharField(max_length=255, null=True, blank=True)
    year = CharField(max_length=64, null=True, blank=True)
    type = CharField(max_length=32, choices=TYPES, default='photo')
    source = CharField(max_length=32, choices=SOURCES, default='original')
    style = CharField(max_length=128, choices=STYLES, default='contemporary')
    n_copies = DecimalField(max_digits=10, decimal_places=2, null=True)

    fpath = CharField(max_length=1000, null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    user = ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title

    def __unicode__(self):
        return self.title

    def username(self):
        return self.user.username

# products is a table to represent selling list
class Product(Model):
    code = CharField(max_length=255, null=True, blank=True)
    price = DecimalField(max_digits=10, decimal_places=3, null=True)
    currency = CharField(max_length=16, choices=CURRENCIES, default='usd')
    status = CharField(max_length=16, choices=STATUS, default='active')
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now_add=True)

    owner = ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    item = ForeignKey(Item, null=True, blank=True, on_delete=models.CASCADE)
    
class Ownership(Model):
    source = CharField(max_length=32, choices=SOURCES, default='original')
    buy_price = DecimalField(max_digits=10, decimal_places=3, null=True)
    buy_currency = CharField(max_length=16, choices=CURRENCIES, default='usd')
    sell_price = DecimalField(max_digits=10, decimal_places=3, null=True)
    sell_currency = CharField(max_length=16, choices=CURRENCIES, default='usd')
    status = CharField(max_length=16, choices=STATUS, default='active')
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now_add=True)

    product = ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
    owner = ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)



class UploadForm(forms.Form):
    file = forms.ImageField()
    title = CharField(max_length=255, null=True, blank=True)
    description = CharField(max_length=1000, null=True, blank=True)
    dimension = CharField(max_length=255, null=True, blank=True)
    author = CharField(max_length=255, null=True, blank=True)
    year = CharField(max_length=64, null=True, blank=True)
    type = CharField(max_length=32, choices=TYPES, default='photo')
    source = CharField(max_length=32, choices=SOURCES, default='original')
    style = CharField(max_length=128, choices=STYLES, default='contemporary')
    n_copies = DecimalField(max_digits=10, decimal_places=2, null=True)

    fpath = CharField(max_length=1000, null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    user = ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

