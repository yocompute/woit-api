from django.shortcuts import render
from crypto import Crypto
import uuid
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from keys.models import Key

from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

def verify(product_id, token):
    r = Key.objects.get(product_id=product_id)
    
    crypto = Crypto(r.key)
    s = crypto.decode(token)
    product_id, owner_id, code = s.split('-') # 
    
    return owner_id == r.product.owner.id and code == r.code
    
def get_key(product_id):
    r = Key.objects.get(product_id=product_id)
    if r is None:
        crypto = Crypto()
        return crypto.key
    else:
        return r.key

def generate_code(product_id, owner_id):
    """ This code should not be shown on UI
    """
    return product_id + '-' + owner_id + '-' + uuid.uuid4().hex

def generate_token(key, code):
    """ This token can be display on UI for user to verify
    """
    crypto = Crypto(key)
    return crypto.encode(bytes(code))


@method_decorator(csrf_exempt, name='dispatch')
class KeyView(View):
    def get(self, req, *args, **kwargs):
        # verify key
        token = req.token
        product_id = req.product_id
        ret = verify(product_id, token)
        return JsonResponse({'ret':ret}, safe=False)

    def post(self, req, *args, **kwargs):
        # add key and code to keys table
        token = req.body.token
        product_id = req.body.product_id
        k = Key()
        k.key = get_key(product_id)
        k.product = Product.objects.get(product_id=product_id)
        owner_id = k.product.owner.id
        k.code = generate_code(product_id, owner_id)
        k.save()
        return JsonResponse({'ret':true}, safe=False)

