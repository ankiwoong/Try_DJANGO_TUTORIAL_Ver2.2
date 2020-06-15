from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .models import BlogPost

# Create your views here.

# GET > 1 object            : 1개 오브젝트 수용
# filter > [] object        : 리스트 형태 오브젝트 수용


def blog_post_detail_page(request, slug):
    queryset = BlogPost.objects.filter(slug=slug)
    if queryset.count() >= 1:
        # raise Http404
        obj = queryset.first()

    # obj = queryset.first()
    # print(post_id.__class__)
    # obj = get_object_or_404(BlogPost, slug=slug)
    template_name = "blog_post_detail.html"
    context = {"object": obj}  # {'title': objecct.title}

    return render(request, template_name, context)
