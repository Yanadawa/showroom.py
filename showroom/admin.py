from django.contrib import admin
from .models import Car, Service

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'merk', 'model', 'tahun', 'harga_dasar')
    search_fields = ('merk', 'model')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('mobil', 'tanggal', 'deskripsi', 'biaya')
    list_filter = ('tanggal',)
