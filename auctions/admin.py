from django.contrib import admin
from .models import User, Listing, Categories, Bid

# Register your models here.

class showBidDetails(admin.ModelAdmin):
    list_display = ('BidUser','bidAmount','BidOnThisList')
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Categories)
admin.site.register(Bid, showBidDetails)