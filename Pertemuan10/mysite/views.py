from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  context = {
    "name": "Ojan"
    }
  return render(request, 'index.html', context=context)