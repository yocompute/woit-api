import os

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from items.models import Item

from django.contrib.auth.models import User
from django.core import serializers

from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

class ItemView(View):
	def get(self, req, *args, **kwargs):
		items = Item.objects.select_related('owner')
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
        
        # owner = ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

class UploadForm(forms.Form):
    file = forms.ImageField()
    owner_id = forms.CharField(max_length=255)
    title = forms.CharField(max_length=255)
    description = forms.CharField(max_length=1000)
    n_copies = forms.DecimalField(max_digits=10)
    size = forms.CharField(max_length=255)
    type = forms.CharField(max_length=20)

@method_decorator(csrf_exempt, name='dispatch')
class UploadView(View):
    def post(self, req, *args, **kwargs):
        uForm = UploadForm(req.POST, req.FILES)
        #if uForm.is_valid():
        item = Item()
        # item.title = uForm.cleaned_data["title"]
        # item.description = uForm.cleaned_data["description"]
        # item.author = uForm.cleaned_data["author"]
        # item.size = uForm.cleaned_data["size"]
        # item.n_copies = uForm.cleaned_data["n_copies"]
        # item.type = uForm.cleaned_data["type"]
        # item.price = uForm.cleaned_data["price"]

        # owner_id = uForm.cleaned_data["owner_id"]
        # item.owner = User.objects.get(id=owner_id)

        # BASE_DIR = os.path.dirname(os.path.dirname(__file__)).replace("\\", "/")
        # folder = "/sample/" + uForm.cleaned_data["username"] + "/"
        # filename = req.FILES['file'].name

        # # create the folder if it doesn't exist.
        # try:
        #     os.mkdir(BASE_DIR + '/sample/')
        #     os.mkdir(BASE_DIR + folder)
        # except:
        #     pass

        # # save the uploaded file inside that folder.
        # full_filename = BASE_DIR + folder + filename
        # fout = open(full_filename, 'wb+')

        # file_content = ContentFile( req.FILES['file'].read() )
        
        # try:
        #     # Iterate through the chunks.
        #     for chunk in file_content.chunks():
        #         fout.write(chunk)
        #     fout.close()
        # except:
        #     pass

        # item.fpath = os.path.join(folder, filename)

        # item.save()
        return JsonResponse({'saved': True}, safe=False)

        #return JsonResponse({'saved': False}, safe=False)