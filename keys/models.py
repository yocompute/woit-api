from django.db import models
from django.db.models import CharField, Model, ForeignKey, DateTimeField, DecimalField
from items.models import Product

class Key(Model):    
    key = CharField(max_length=1024, null=True, blank=True)
    code = CharField(max_length=1024, null=True, blank=True)

    product = ForeignKey(Product, null=True, blank=True)
