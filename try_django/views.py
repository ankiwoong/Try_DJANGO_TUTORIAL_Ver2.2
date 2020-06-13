from django.http import HttpResponse

# Model View Template (MVT)
def home_page(request):
    return HttpResponse("<h1>Hello World</h1>")


def about_page(request):
    return HttpResponse("<h1>About Us</h1>")


def contact_page(request):
    return HttpResponse("<h1>Contact Us</h1>")
