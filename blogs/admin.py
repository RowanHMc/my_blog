from django.contrib import admin
from .models import Post, Category, Subscriber


# Register your models here.
admin.site.register(Post) #only takes one argument
admin.site.register(Category)
admin.site.register(Subscriber)
