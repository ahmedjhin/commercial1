from django.contrib import admin
from .models import User, Listing, Categories, Bid,comments

# Register your models here.

class showBidDetails(admin.ModelAdmin):
    list_display = ('BidUser','bidAmount','BidOnThisList')

class commentsDetails(admin.ModelAdmin):
    list_display = ('Comment','owner','onList')

admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Categories)
admin.site.register(Bid, showBidDetails)
admin.site.register(comments, commentsDetails)