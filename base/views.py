from django.shortcuts import render, redirect
from django.http import HttpResponse
import random

from .forms import ImageForm

from django.conf import settings

from .forms import RegistrationForm
from django.contrib.auth import login

def index(request):
    random_number = random.randint(1, 14)
    print(random_number)
    # random_number= int(5)

    context = {'range':range(1,15), 'random_number':random_number, 'MEDIA_URL': settings.MEDIA_URL}
    return render(request, 'index.html', context)

def result(request):
    # return HttpResponse("result")
    return render(request, 'result.html')

def signup(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('/')

    else:
        form = RegistrationForm()

    return render(request, 'registration/signup.html', {'form' : form})


def tryin(request):
    return render(request,'try.html')

def showImgs(request):

    return render(request, 'show.html', {'range':range(1,15), 'MEDIA_URL': settings.MEDIA_URL})


def uploadImg(request):

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            print("in post")
            form.save()

            img_obj = form.instance

            return render(request, 'form.html', {'form':form, 'img_obj':img_obj})
        
    else:
        form = ImageForm()
    
    return render(request,'form.html',{'form':form})
    