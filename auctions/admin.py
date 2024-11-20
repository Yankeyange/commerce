from django.contrib import admin
from .models import Auctions,Details

class AdminAuctions(admin.ModelAdmin):
  list_display = ('name', "title", "image","description","date","price")

admin.site.register(Auctions, AdminAuctions)
admin.site.register(Details)

