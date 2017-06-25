import os

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from items.models import Item, UploadForm

from django.contrib.auth.models import User
from django.core import serializers
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class ItemView(View):
	def get(self, req, *args, **kwargs):
		items = Item.objects.select_related('user')
		s = serializers.serialize("json", list(items))
		return JsonResponse({'items':s}, safe=False)
	
class OfferView(View):
	def get(self, req, *args, **kwargs):
		items = Item.objects.select_related('owner')
		data = serializers.serialize("json", items)
		return JsonResponse(data, safe=False)

        # title = CharField(max_length=255, null=True, blank=True)
        # description = CharField(max_length=1000, null=True, blank=True)
        # auther = CharField(max_length=255, null=True, blank=True)
        # size = CharField(max_length=255, null=True, blank=True)
        # n_copies = DecimalField(max_digits=10, decimal_places=2, null=True)
        # code = CharField(max_length=255, null=True, blank=True)
        # type = CharField(max_length=4, choices=TYPES, default='O')
        # price = DecimalField(max_digits=10, decimal_places=2, null=True)
        # fpath = CharField(max_length=1000, null=True, blank=True)
        # created = DateTimeField(auto_now_add=True)
        # updated = DateTimeField(auto_now=True)
        
        # user = ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)



@method_decorator(csrf_exempt, name='dispatch')
class UploadView(View):
    def post(self, req, *args, **kwargs):
        uForm = UploadForm(req.POST, req.FILES)
        #if uForm.is_valid():
        item = Item()
        item.title = uForm.data["title"]
        item.description = uForm.data["description"]
        item.dimension = uForm.data["dimension"]
        item.author = uForm.data["author"]
        item.year = uForm.data["year"]
        item.type = uForm.data["type"]
        item.source = uForm.data["source"]
        item.style = uForm.data["style"]
        item.n_copies = uForm.data["n_copies"]
        item.created = uForm.data["created"]
        item.updated = uForm.data["updated"]
        user_id = uForm.data["user_id"]
        item.user = User.objects.get(id=user_id)
        
        folder = os.path.join('photos', item.user.username)
        file = req.FILES.get('file')
        fname = file.name
        fpath = os.path.join(settings.MEDIA_ROOT, folder)

        if not os.path.exists(fpath):
        	os.makedirs(fpath)
        # save the uploaded file inside that folder.
        full_filename = os.path.join(fpath, fname)
        
        if not os.path.exists(full_filename):
	        fout = open(full_filename, 'wb+')
	        fout.write(file.read())
	        fout.close()

	        item.fpath = os.path.join(folder, fname)
	        item.save()
        else:
        	return JsonResponse({'saved': False}, safe=False)
        return JsonResponse({'saved': True}, safe=False)
