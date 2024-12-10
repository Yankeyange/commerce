from django.contrib import admin
from .models import Auctions, Bids, Comment, Category

class AdminAuctions(admin.ModelAdmin):
  list_display = ('name', "title", "image","description","date","price")

admin.site.register(Auctions, AdminAuctions)
admin.site.register(Bids)
admin.site.register(Comment)
admin.site.register(Category)
#admin.site.register(Entry)


