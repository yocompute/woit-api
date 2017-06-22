from django.contrib.auth.models import User

from django.db import models
from django.db.models import CharField, Model, ForeignKey, DateTimeField, DecimalField

TYPES = (('photo','Photo'), ('paint', 'Paint'))
SOURCES = (('original','Original'), ('market', 'From Market'))
CURRENCIES = (('usd','USD'), ('cad', 'CAD'), ('cny','CNY'))
STYLES = (('contemporary', 'Contemporary'), ('modern', 'Modern'))
class Item(Model):
    title = CharField(max_length=255, null=True, blank=True)
    description = CharField(max_length=1000, null=True, blank=True)
    code = CharField(max_length=255, null=True, blank=True)
    dimension = CharField(max_length=255, null=True, blank=True)
    author = CharField(max_length=255, null=True, blank=True)
    date = CharField(max_length=64, null=True, blank=True)
    type = CharField(max_length=32, choices=TYPES, default='photo')
    source = CharField(max_length=32, choices=SOURCES, default='original')
    style = CharField(max_length=128, choices=STYLES, default='contemporary')
    price = DecimalField(max_digits=10, decimal_places=2, null=True)
    currency = CharField(max_length=16, choices=CURRENCIES, default='usd')
    n_copies = DecimalField(max_digits=10, decimal_places=2, null=True)

    fpath = CharField(max_length=1000, null=True, blank=True)
    created = DateTimeField(auto_now_add=True)
    updated = DateTimeField(auto_now=True)

    owner = ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title

    def __unicode__(self):
        return self.title

    def owner_username(self):
        return self.owner.username