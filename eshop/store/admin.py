from django.contrib import admin
from .models import *
from django.utils.html import format_html
# Register your models here.

class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name' , 'price' , 'category']

    def image_tag(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.image.url))
    image_tag.short_description = 'Product Image Preview'
    readonly_fields = ['image_tag']

class AdminCategory(admin.ModelAdmin):
    list_display = ['id','name']

class AdminCustomers(admin.ModelAdmin):
    list_display = ['id','first_name','phone','email']

class AdminOrder(admin.ModelAdmin):
    list_display = ['id','customer','quantity','price','status']


admin.site.register(Category,AdminCategory)
admin.site.register(Product,AdminProduct)
admin.site.register(Customer,AdminCustomers)
admin.site.register(Order,AdminOrder)