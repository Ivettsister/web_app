from django.contrib import admin

from goods.models import Categories, Products

# регистрация моделей, prepopulated_fields - автозаполнение (шаблон) для полей

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

