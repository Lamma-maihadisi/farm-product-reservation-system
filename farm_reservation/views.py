from django.http import HttpResponse
from django.shortcuts import  render

def index(request):
    return render(request, 'base.html')


def product(request):
    return render(request, 'product.html')


def reservation(request):
    return render(request, 'reservation.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')