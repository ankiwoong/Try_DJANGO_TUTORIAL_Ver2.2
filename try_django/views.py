from django.http import HttpResponse

# Model View Template (MVT)
def home_page(request):
    return HttpResponse("<h1>Hello World</h1>")
