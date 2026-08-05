from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def first(request):
    if request.method=='GET':
        return HttpResponse('Hello world')