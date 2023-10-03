from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    pass


class Categories(models.Model):
    CateGname = models.CharField(max_length=20)
    Listings = models.ManyToManyField('Listing', blank=True)

    def __str__(self):
        return self.CateGname

class Bid(models.Model):
    bidAmount = models.IntegerField(max_length=10)
    BidUser = models.ForeignKey(User ,on_delete=models.CASCADE,blank=True, null=True, related_name="BidUser")
    BidOnThisList = models.ForeignKey('Listing',on_delete=models.CASCADE,blank=True, null=True, related_name="BidOnThisList")

class Listing(models.Model):
    ListName = models.CharField(max_length=20)
    ListCategory = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True,blank=True,related_name='ListingCategory')
    ListOwner = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True, related_name="ListOwner")
    ListDiscription = models.CharField(max_length=200)
    ListImagesUrl = models.CharField(max_length=1000, blank=True, null=True,)
    ListPrice = models.CharField(max_length=20)
    ListBid = models.ForeignKey(Bid, on_delete=models.CASCADE,blank=True, null=True, related_name="ListBid")
    def __str__(self):
        return self.ListName