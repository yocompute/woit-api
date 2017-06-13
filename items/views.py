from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.generic import View
from items.models import Item
from django.core import serializers

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