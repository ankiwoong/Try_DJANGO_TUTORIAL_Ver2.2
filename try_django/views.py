from django.http import HttpResponse
from django.shortcuts import render

# Model View Template (MVT)
def home_page(request):
    return HttpResponse(request, "hello_world.html")


def about_page(request):
    return HttpResponse("<h1>About Us</h1>")


def contact_page(request):
    return HttpResponse("<h1>Contact Us</h1>")
