from django.contrib import admin
from .models import Product, Client, Order

@admin.action(description="Сбросить количество в ноль")
def reset_count(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count']
    ordering = ['price', 'name']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_count]

    fields = ['name', 'description', 'price', 'count', 'date_income', 'rating']
    readonly_fields = ['date_income']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'birthday']
    ordering = ['name']
    search_fields = ['name']
    search_help_text = 'Поиск по имени (name)'

    # fields = ['']
    readonly_fields = ['register_date']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'order_price', 'order_date']
    ordering = ['order_date']

    readonly_fields = ['order_date']

admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)

