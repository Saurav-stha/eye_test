from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    random_number = random.randint(1, 14)
    print(random_number)
    # random_number= int(5)

    context = {'range':range(1,15), 'random_number':random_number}
    return render(request, 'index.html', context)

def saveData(request):
    return HttpResponse("working")
    

def tryin(request):
    return render(request,'try.html')