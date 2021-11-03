from django.contrib import admin
from .models import Sneaker, Category


# Register your models here.


class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'size', 'time_create', 'price')
    search_fields = ('title', 'size', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Sneaker, ShopAdmin)
admin.site.register(Category, CategoryAdmin)