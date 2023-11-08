from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse   

def jampando(request):
    return HttpResponse('hii')