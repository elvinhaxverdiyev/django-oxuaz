from django.contrib import admin
from .models import Category, Article


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    search_fields = ("name",) 
    ordering = ("created_at",)
    
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author_name", "category", "created_at")
    search_fields = ("title", "content", "author_name__username")
    list_filter = ("category", "created_at")
    ordering = ("-created_at",) 