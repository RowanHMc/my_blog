from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.
def hello(request):
    return HttpResponse('Hello world!')

def intro(request):
    student = {
        "school":"School: Zindua School",
        "name":"Name: Rowan",
        "email":"Email: RowanHadegu@gmail.com"
    }
    return render(request, 'intro.html', student)
def home(request):
    student = {
        "school":"Zindua School",
        "name":"Rowan Hadegu",
        "email":"rh1234@gmail.com"
    }
    return render(request, 'index.html', student)

def contact(request):
    contact_details = {
        "email": "RowH@gmail.com",
        "number": "+254712345678"
    }
    return render(request, 'contact.html', contact_details)

def about(request):
    about_details = {
        "name": "Zindua School",
        "location": "Parklands Plaza, Westlands",
        "course": "Software Engineering"
    }
    return render(request, 'about.html', about_details)

def blogs(request):
    posts = Post.objects.all()
    return render(request, 'blogs.html',{"posts": posts})

def blog_detail(request, slug):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog_detail.html", {"post": post})    