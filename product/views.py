from django.shortcuts import render
from django.http import HttpResponse
import requests, json

# Create your views here.
def home(request):
    return render(request, 'index.html')

def heart(request):
    response = requests.get("https://ood-project-api-6452e2a331a7.herokuapp.com/products/cate=Heart")
    return render(request, 'heart.html', {'data': response.json()})

def diabetes(request):
    response = requests.get("https://ood-project-api-6452e2a331a7.herokuapp.com/products/cate=Diabetes")
    return render(request, 'diabetes.html', {'data': response.json()})

def vitamins(request):
    response = requests.get("https://ood-project-api-6452e2a331a7.herokuapp.com/products/cate=Vitamins")
    return render(request, 'vitamins.html', {'data': response.json()})

def supplements(request):
    response = requests.get("https://ood-project-api-6452e2a331a7.herokuapp.com/products/cate=Supplements")
    return render(request, 'supplements.html', {'data': response.json()})

def flu(request):
    response = requests.get("https://ood-project-api-6452e2a331a7.herokuapp.com/products/cate=Flu")
    return render(request, 'flu.html', {'data': response.json()})

def dental(request):
    response = requests.get("https://ood-project-api-6452e2a331a7.herokuapp.com/products/cate=Dental")
    return render(request, 'dental.html', {'data': response.json()})

def homo(request):
    return render(request, 'homo.html')

def otc(request):
    return render(request, 'otc.html')