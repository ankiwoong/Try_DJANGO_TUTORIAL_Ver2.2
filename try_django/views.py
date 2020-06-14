from django.http import HttpResponse
from django.shortcuts import render

# Model View Template (MVT)
# Dont Repeat Yourself = DRY
def home_page(request):
    my_title = "Hello there ..."
    # doc = "<h1>{title}</h1>".format(title=my_title)
    # django_render_doc = "<h1>{{ title }}</h1>".format(title=my_title)
    return render(request, "hello_world.html", {"title": my_title})


def about_page(request):
    return render(request, "about.html", {"title": "About Us"})


def contact_page(request):
    return render(request, "hello_world.html", {"title": "Contact Us"})
