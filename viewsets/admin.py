from django.contrib import admin
from .models import songs

@admin.register(songs)

class songsadmin(admin.ModelAdmin):
    list_display = ['id','songtitle','singer','dateandtime']