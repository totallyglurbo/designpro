from django.contrib import admin
from .models import Post, Category, ReallyUser

admin.site.register(ReallyUser)
admin.site.register(Post)
admin.site.register(Category)

