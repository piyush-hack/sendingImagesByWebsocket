# chat/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'example/index.html')


def test(request):
    return render(request, 'example/test.html')


def base(request):
    return render(request, 'example/base.html')
