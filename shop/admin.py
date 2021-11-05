from django.contrib import admin
from .models import Sneaker, Category, Size


# Register your models here.


class ShopAdmin(admin.ModelAdmin):
    list_display = ('title', 'time_create', 'price')
    search_fields = ('title', 'size', 'price')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class SizeAdmin(admin.ModelAdmin):
    list_display = ('id', 'size')
    list_display_links = ('id', 'size')
    search_fields = ('size',)


admin.site.register(Sneaker, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Size)