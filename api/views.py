# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.
import requests
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import urllib2 

@csrf_exempt
def dput(request):
    request_body = json.loads(request.body)
    a = request_body ['Type']
    if a == 'SubscriptionConfirmation':
        results = requests.get(request_body['SubscribeURL'], 
              params={'q': 'query', 'first': 'page'}, 
              headers={'User-Agent': 'user_agent'})
        print results
        with open("Subscription.log", "a") as myfile:
            myfile.write(request.body + "\n" + "confirmation:" + "\n")
    elif a == 'Notification':
        with open("Notifications.log", "a") as myfile:
            myfile.write(request.body + "\n")
    else:
        with open("Other.log", "a") as myfile:
            myfile.write(request.body + "\n")
    return HttpResponse()