#from django.http import HttpResponse
from django.shortcuts import render


def holamundo(request):
    #return HttpResponse("Hello World!")
    return render(request, 'home.html')