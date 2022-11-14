from django.contrib import admin

# Register your models here.
from.models import *

class catgadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']
admin.site.register(Categ,catgadmin)

class prodAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','img','available']
    list_editable=['price','stock','img','available']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Products,prodAdmin)

#cart
admin.site.register(CartList)
admin.site.register(CartItems)
#endcart