from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html',name='home')


def about(request):
    return HttpResponse('welcome to about page')


