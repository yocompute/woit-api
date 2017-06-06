# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.db.models import Q
from django.core import serializers
from django.http import JsonResponse
from django.views.generic import View

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User


@method_decorator(csrf_exempt, name='dispatch')
class AccountView(View):
	def get(self, req, *args, **kwargs):
		account = req.GET.get("account")
		users = User.objects.filter(Q(username__iexact=account) | Q(email__iexact=account))
		data = serializers.serialize("json", users)
		return JsonResponse(data, safe=False)
	
	def post(self, req, *args, **kwargs):
		# for login
		d = json.loads(req.body)
		r = User.objects.get(Q(username__iexact=d['account']) | Q(email__iexact=d['account']))
		if r and r.check_password(d['password']):
			r.password = ''
			s = serializers.serialize("json", [r])
			return JsonResponse({'token':'good', 'users':s }, safe=False)
		else:
			return JsonResponse({'token':'', 'users':''}, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
	def get(self, req, *args, **kwargs):
		users = User.objects.filter()
		data = serializers.serialize("json", users)
		return JsonResponse(data, safe=False)
	
	def post(self, req, *args, **kwargs):
		d = json.loads(req.body)
		r = User.objects.filter(username__iexact=d['username'])
		if r:
			return JsonResponse({'token':''}, safe=False)
		else:
			User.objects.create_user(d['username'], d['email'], d['password']);
			return JsonResponse({'token':'good'}, safe=False)




