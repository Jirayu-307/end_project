from django.contrib import admin
from app_rooms.models import Room

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'is_multiple_bed', 'check_in_date', 'check_out_date']
    search_fields = ['title']
    list_filter = ['is_multiple_bed']
    
admin.site.register(Room, RoomAdmin)