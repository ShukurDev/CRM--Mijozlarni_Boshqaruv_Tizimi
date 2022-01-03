from django.contrib import admin
from .models import *
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name','phone','email']

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)

