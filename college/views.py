from django.shortcuts import render
from django.http.response import *

# Create your views here.


def my_page(request):
    return HttpResponse('Okay')
