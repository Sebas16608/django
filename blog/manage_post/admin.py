from django.contrib import admin
from manage_post.models import Category, Article, Rating, Profile

# Register your models here.

admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Rating)
admin.site.register(Profile)