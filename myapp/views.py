from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests

def defaultView(request):
    return HttpResponse("<h1>Default View</h1>")


def getProduct(request):
    response = requests.get("https://ood-project-api-6452e2a331a7.herokuapp.com/products/sprin")
    return JsonResponse(response.json(), safe=False)


def getUser(request):
    response = requests.get("https://ood-project-api-6452e2a331a7.herokuapp.com/users/kaneri")
    return JsonResponse(response.json(), safe=False)


def getPharma(request):
    response = requests.get("https://ood-project-api-6452e2a331a7.herokuapp.com/pharamacist/micheal")
    return JsonResponse(response.json(), safe=False)



