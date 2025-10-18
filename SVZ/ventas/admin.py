from django.contrib import admin

# Register your models here.
from .models import ventas
@admin.register(ventas)
class ventasAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'fecha_registro')
    search_fields = ('nombre',)
    list_filter = ('fecha_registro',)
