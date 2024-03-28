from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {"title": "home", "text": "Главная страница - Home Page"}

    return render(request, "main/index.html", context)


def about(request):
    return HttpResponse("About page")
