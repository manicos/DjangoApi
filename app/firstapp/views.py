# Create your views here.
#IMPORT models

#IMPORT LIBRARIRES/FUNCTIONS
from django.shortcuts import render , HttpResponse
from django.http import JsonResponse
import json
import requests
#IMPORT DJANGO PASSWORD HASH GENERATOR AND COMPARE
from django.contrib.auth.hashers import make_password, check_password
from .models import Dogs,Types

#check_password(noHashPassword,HashedPassword) this funcion validate if the password match to the hash

#def vista(request):
#    return render(request,'clase.html')

def vista(request):

    query = "batman"
    apiKey = "c809e516f37fa7407b060cc0dd57bce4"

    #API URL
    url = 'https://api.themoviedb.org/3/search/movie?query=' + query + '&api_key=' + apiKey;

    response = requests.get(url)
    result = response.json()
    cuantos = len(result['results']);

    #post_data = {'remote_api_file_field': self.file}
    #requests.post(REMOTE_API_URL, data=post_data)

    #url = 'https://www.googleapis.com/urlshortener/v1/url'
    #data = {'longUrl': 'http://www.google.com/'}
    #headers = {'Content-Type': 'application/json'}

    #response = requests.post(url, data=json.dumps(data), headers=headers)

    return render(request, 'clase.html', {'cuantos': cuantos , "movies": result })


def dogs(request):

    if request.method == 'GET':

        apikey = request.headers.get('api_key')
        apikey = "33390d09esdioewu0qe0uqu0"
        if apikey is not None:

            if apikey != "33390d09esdioewu0qe0uqu0":
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'API KEY NOT VALID'
                return JsonResponse(responseData, status=400)

            responseData = {}
            responseData['success'] = 'true'
            responseData['key'] = apikey
            responseData['data'] = list(Dogs.objects.all().values())
            return JsonResponse(responseData, status=200)

        responseData = {}
        responseData['success'] = 'false'
        responseData['message'] = 'No api Key'
        return JsonResponse(responseData, status=400)

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
            try:
                one_entry = Dogs.objects.get(id=json_object["dog_id"])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'The dog_id its not valid'
                return JsonResponse(responseData, status=400)
            Dogs.objects.filter(id=json_object["dog_id"]).delete()
            responseData = {}
            responseData['success'] = 'true'
            responseData['message'] = 'The dog has been deleted'
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

def dogsGet(request):

    if request.method == 'POST':

        try:
            json_object = json.loads(request.body)
            try:
                one_entry = Dogs.objects.get(id=json_object["dog_id"])
            except:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'The dog_id its not valid'
                return JsonResponse(responseData, status=400)
            responseData = {}
            responseData['success'] = 'true'
            responseData['data'] = {}
            responseData['data']['name'] = one_entry.name
            responseData['data']['size'] = one_entry.size
            responseData['data']['color'] = one_entry.color
            responseData['data']['type_id'] = one_entry.type_id

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

def dogsGetId(request, dogid):

    if request.method == 'GET':

        try:
            one_entry = Dogs.objects.get(id=dogid)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'The dog_id its not valid'
            return JsonResponse(responseData, status=400)

        responseData = {}
        responseData['success'] = 'true'
        responseData['data'] = {}
        responseData['data']['name'] = one_entry.name
        responseData['data']['size'] = one_entry.size
        responseData['data']['color'] = one_entry.color
        responseData['data']['type_id'] = one_entry.type_id

        return JsonResponse(responseData, status=200)

    else:

        responseData = {}
        responseData['success'] = 'false'
        responseData['mesage'] = 'Wrong Method'
        return JsonResponse(responseData, status=400)

def dogsUpdate(request,dogid):

    if request.method == 'POST':
        try:
            one_entry = Dogs.objects.get(id=dogid)
        except:
            responseData = {}
            responseData['success'] = 'false'
            responseData['message'] = 'The dog_id its not valid'
            return JsonResponse(responseData, status=400)
        try:
            json_object = json.loads(request.body)
            contador = 0
            #AQUI VA EL CODIGO DEL UPDATE
            try:
                value = json_object["dog_name"]
                Dogs.objects.filter(id=dogid).update(name=json_object["dog_name"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            try:
                value = json_object["dog_size"]
                Dogs.objects.filter(id=dogid).update(size=json_object["dog_size"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            try:
                value = json_object["dog_color"]
                Dogs.objects.filter(id=dogid).update(color=json_object["dog_color"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            try:
                value = json_object["dog_type"]
                Dogs.objects.filter(id=dogid).update(type_id=json_object["dog_type"])
                contador = contador + 1
            except KeyError:
                responseData = {}

            if contador == 0:
                responseData = {}
                responseData['success'] = 'false'
                responseData['message'] = 'Nada por actualizar'
                return JsonResponse(responseData, status=400)
            else:
                responseData = {}
                responseData['success'] = 'true'
                responseData['message'] = 'Datos actualizados'
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
