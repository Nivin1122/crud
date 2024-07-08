from django.contrib import admin
from .models import Coaches,Players,Booking

# Register your models here.
admin.site.register(Coaches)
admin.site.register(Players)
admin.site.register(Booking)

class CoachesAdmin(admin.ModelAdmin):
    list_display = ('coach_name', 'level')