# Create your views here.
#IMPORT models

#IMPORT LIBRARIRES/FUNCTIONS
from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password
from .models import Dogs,Types

#check_password(noHashPassword,HashedPassword) this funcion validate if the password match to the hash

#def vista(request):
#    return render(request,'clase.html')

def vista(request):
    
    #https://docs.djangoproject.com/en/3.0/ref/templates/language/#templates
    return render(request, 'clase.html', {'title': "Bumblebee" , "otra": "asdassdsdsdd" })


def dogs(request):
    
    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Dogs.objects.all().values())
        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)


def dogsAdd(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            newDog = Dogs(name=json_object['dog_name'], type_id=json_object['dog_type_id'], color=json_object['dog_color'], size= json_object['dog_size'])
            #INSERT INTO dogs (name, type_id,color,size) values ('Solovino',4,'black','big')
            newDog.save()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'Dog inserted'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsDelete(request):

    if request.method == 'DELETE':

        try:
            json_object = json.loads(request.body)
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = 'Valid Json'
            return JsonResponse(responseData, status=200)
        except ValueError as e:
            responseData = {}
            responseData['success'] = 'false'
            responseData['data'] = 'Invalid Json'
            return JsonResponse(responseData, status=400)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def types(request):

    if request.method == 'GET':

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = list(Types.objects.all().values())
        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)
