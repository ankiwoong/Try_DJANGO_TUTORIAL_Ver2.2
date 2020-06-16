from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm

# Model View Template (MVT)
# Dont Repeat Yourself = DRY
def home_page(request):
    my_title = "Hello there ..."
    context = {"title": "my_title"}
    if request.user.is_authenticated:
        context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
    # template_name = "title.txt"
    # template_obj = get_template(template_name)
    # rendered_string = template_obj.render(context)
    # print(rendered_string)
    # doc = "<h1>{title}</h1>".format(title=my_title)
    # django_render_doc = "<h1>{{ title }}</h1>".format(title=my_title)
    # return render(request, "hello_world.html", {"title": rendered_string})
    return render(request, "home.html", context)


def about_page(request):
    return render(request, "about.html", {"title": "About Us"})


def contact_page(request):
    # print(request.POST)
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {"title": "Contact Us", "form": form}
    return render(request, "form.html", context)


def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)
