from django.contrib import admin

from .models import Product
from .models import Price
from .models import ProductType

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('updateDate',)
    search_fields = ('title',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Price)
admin.site.register(ProductType)