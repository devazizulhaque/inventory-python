from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.

# def home(request):
#     return HttpResponse('Hello, Django!')

def home(request):
    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.img = 'images/destination_1.jpg'
    dest1.desc = 'The City That Never Sleeps'
    dest1.price = 700
    dest1.offer = False
    return render(request, 'hero/home.html', {'dest1': dest1})

# def add(request):
#     val1 = int(request.POST['num1'])
#     val2 = int(request.POST['num2'])
#     res = val1 + val2
#     return render(request, 'hero/result.html', {'result': res, 'title': 'Addition Result'})
