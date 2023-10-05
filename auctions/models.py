from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    pass


class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    Listings = models.ManyToManyField('Listing', blank=True)
    CateGname = models.CharField(max_length=20)

    def __str__(self):
        return self.CateGname

class Bid(models.Model):
    id = models.BigAutoField(primary_key=True)
    BidUser = models.ForeignKey(User ,on_delete=models.CASCADE,blank=True, null=True, related_name="BidUser")
    bidAmount = models.IntegerField()
    BidOnThisList = models.ForeignKey('Listing',on_delete=models.CASCADE,blank=True, null=True, related_name="BidOnThisList")

class Listing(models.Model):
    id = models.BigAutoField(primary_key=True)
    ListBid = models.ForeignKey(Bid, on_delete=models.CASCADE,blank=True, null=True, related_name="ListBid")
    ListName = models.CharField(max_length=20)
    isActive = models.BooleanField(default=True)
    ListOwner = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True, related_name="ListOwner")
    ListPrice = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    ListCategory = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True,blank=True,related_name='ListingCategory')
    ListImagesUrl = models.CharField(max_length=1000, blank=True, null=True,)
    ListDiscription = models.CharField(max_length=200)

    def __str__(self):
        return  str(self.ListName)