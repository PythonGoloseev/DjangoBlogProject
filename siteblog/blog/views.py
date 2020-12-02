from django.shortcuts import render
from django.http import HttpRequest


def helloWorld(request: HttpRequest):
    return render(request, 'blog/index.html')



