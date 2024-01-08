from django.contrib import admin
from .models import *
# Register your models here.
class BukuAdmin(admin.ModelAdmin):
   
    exclude = ('slug',)  

admin.site.register(Buku,BukuAdmin)
admin.site.register(GambarBuku)
