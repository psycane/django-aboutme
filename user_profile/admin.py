from django.contrib import admin
from .models import Booking, Payment


class BookingAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'name',
                    'phone_no',
                    'email']

    class Meta:
        model = Booking


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'booking',
                    'fair_amount']

    class Meta:
        model = Payment

# Register your models here.
admin.site.register(Booking, BookingAdmin)
admin.site.register(Payment, PaymentAdmin)
