from django.contrib import admin

# Register your models here.
from .models import *

class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_available')
    list_display_links = ('id', 'name')
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('orderId', 'goodsName', 'size', 'price')
    list_display_links = ('orderId', )
    search_fields = ('orderId', )

class UsersAdmin(admin.ModelAdmin):
    list_display = ('userId', 'order')
    list_display_links = ('userId', 'order')
    search_fields = ('userId',)

class StatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'order')
    list_display_links = ('status', 'order')
    search_fields = ('order__orderId',)

class StatusVariablesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

admin.site.register(Goods, GoodsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(StatusVariables, StatusVariablesAdmin)

