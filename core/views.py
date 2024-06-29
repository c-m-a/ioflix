from django.shortcuts import render


def home(request):
    return render(request, "pages/home.html")

def landing(request):
    return render(request, "pages/landing.html")

