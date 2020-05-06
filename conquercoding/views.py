from django.shortcuts import render
from django.http import HttpResponse
from random import choice

# Create your views here.
def home(request):
    return render(request,'conquercoding/home.html')

def password(request):
    password =''
    characters = []
    if request.GET.get('lowercase'):
        characters.extend(list('abcdefghijklmnopqrstuvwxyz'))
    length = int(request.GET.get('length'))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWSYZ'))
    if request.GET.get('number'):
        characters.extend(list('0123456789'))
    if len(characters) !=0 :
        for count in range(length):
            password += choice(characters)

    return render(request,'conquercoding/password.html', {'password' : password})
