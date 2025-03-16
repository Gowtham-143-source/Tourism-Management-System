from django.contrib import admin
from .models import TourPackage, Booking

@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'combo_available', 'status')
    list_filter = ('category', 'combo_available', 'status')
    search_fields = ('name', 'places')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'package', 'email', 'phone', 'booking_date')
    search_fields = ('name', 'email', 'phone')


# Register your models here.
