from django.contrib.auth.models import User

from django.db import models
from django.db.models import CharField, Model, ForeignKey, DateTimeField, DecimalField

TYPES = (('O','Original'), ('M', 'From Market'))

class Item(Model):
        title = CharField(max_length=255, null=True, blank=True)
        description = CharField(max_length=1000, null=True, blank=True)
        code = CharField(max_length=255, null=True, blank=True)
        type = CharField(max_length=4, choices=TYPES, default='O')
        price = DecimalField(max_digits=10, decimal_places=2, null=True)
        created = DateTimeField(auto_now_add=True)
        updated = DateTimeField(auto_now=True)
        owner = ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

        def __str__(self):
                return self.title

        def owner_username(self):
            return self.owner.username