from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def welcomeHome(request):

    return HttpResponse("<h1>Welcome in our project</h1>")