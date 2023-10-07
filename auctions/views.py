from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import User, Listing, Categories


def index(request):
    Activelists = Listing.objects.filter(isActive=True)
    return render(request, "auctions/index.html",{"Activelists":Activelists})

def CreatList(request):
    if request.method == "POST":
        ListNameq =  request.POST.get("ListName")
        ListCategoryq = request.POST.get("ListCategory")
        ListImageq = request.POST.get("ListImage")
        ListPriceq = request.POST.get("ListPrice")
        ListDiscriptionq = request.POST.get("ListDiscription")
        
        ListOwnerq = request.user
        listcatfilterd = Categories.objects.get(CateGname=ListCategoryq)
        NewList = Listing(ListDiscription=ListDiscriptionq,
                          ListName=ListNameq,
                          ListCategory=listcatfilterd,
                          ListImagesUrl=ListImageq,
                          ListPrice=ListPriceq,
                          ListOwner=ListOwnerq)
        NewList.save()
        
        catagores = Categories.objects.all()
        return render(request, "auctions/index.html",{
                                                          'catagores':catagores} )
    else:
        catagores = Categories.objects.all()
        return render(request, "auctions/CreatListin.html",{'catagores':catagores})
    
def DisplayList(request , pk):
    if request.method == "GET":
        List = Listing.objects.filter(pk=pk)
        return render(request, "auctions/DisplayList.html",{'List':List})

def AddListTowatchList(request , pk):
    if request.method == "POST":
        userThatOwnsTheWatchList = User.objects.filter(Username=request.user)
        theList = Listing.objects.filter(pk=pk)
        theList.ListWatchList.add(userThatOwnsTheWatchList) # type: ignore
        theList.save() # type: ignore
        return  HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password) # type: ignore
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")