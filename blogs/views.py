from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Post
from .forms import PostForm


# Create your views here.
# def hello(request):
#     return HttpResponse('Hello world!')

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

def blog_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog_detail.html", {"post": post})  



@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            # Assign the currently logged-in user.
            post.user = request.user
            post.save()
            return redirect("blog_detail", post_id=post.id)
    else:
        form = PostForm()

    return render(
        request,
        "post_form.html",
        {
            "form": form,
            "page_title": "Create Post",
            "button_text": "Publish Post",
        },
    )


@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # Only the author can edit the post.
    if post.user != request.user:
        return redirect("blog_detail", post_id=post.id)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect("blog_detail", post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "post_form.html",
        {
            "form": form,
            "page_title": "Edit Post",
            "button_text": "Update Post",
            "post": post,
        },
    )  