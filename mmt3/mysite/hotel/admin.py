from django.contrib import admin

# Register your models here.


from .models import Hotel_info , Hotel_room ,Venue

class Hotel_info_admin(admin.ModelAdmin):
    list_display = ('hotell_name','hotell_address','hotell_description')
    list_filter = ('hotell_name','hotell_address')
    search_fields = ('hotell_name','hotell_address')
    actions = ('Hold for the time')
    fieldsets = (
        (None, {'fields':('hotell_name','hotell_address','hotell_description')}),
    )

    def hide_hotel(self , request,queryset):
        queryset.update(is_draft = False)



class room_info_admin(admin.ModelAdmin):
    list_display = ('room_type','room_description','room_price')
    list_filter = ('room_type',)
    search_fields = ('room_unique_code',)
    actions = ('Hold for the time')
    fieldsets = (
        (None, {'fields':('room_unique_code','room_type','room_description','room_price')}),
    )

    def hide_hotel(self , request,queryset):
        queryset.update(is_draft = False)

admin.site.register(Hotel_info, Hotel_info_admin)
admin.site.register(Hotel_room, room_info_admin)
admin.site.register(Venue)