from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render ,redirect
from django.urls import reverse
from django.db.models import Max


from .models import User, Listing, Categories, Bid,comments


def index(request):
    Activelists = Listing.objects.filter(isActive=True)
    if User is authenticate:
        test = Listing.objects.exclude(ListOwner=request.user).all()
        return render(request, "auctions/index.html",{ "Activelists":Activelists,"test":test })
    else:
        return render(request, "auctions/index.html",{ "Activelists":Activelists})
    

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
        List = Listing.objects.get(pk=pk)
        IsinwatchList = request.user in List.ListWatchList.all()
        bidList = Bid.objects.filter(BidOnThisList=List).aggregate(haighstbid=Max('bidAmount'))['haighstbid']
        bidListmaxs = Bid.objects.filter(bidAmount=bidList,BidOnThisList=List)
        comment = reversed(comments.objects.filter(onList=List))

        return render(request, "auctions/DisplayList.html",{'List':List,
                                                            'IsinwatchList':IsinwatchList,
                                                            'bidList':bidList,
                                                            'bidListmaxs':bidListmaxs,
                                                            'comment':comment,})
    return render(request, "auctions/DisplayList.html")

def AddListTowatchList(request , pk):
    if request.method == "POST":
        userThatOwnsTheWatchList = request.user
        theList = Listing.objects.get(pk=pk)
        theList.ListWatchList.add(userThatOwnsTheWatchList)
        theList.save()
        return  HttpResponseRedirect(reverse("DisplayList" , args=(pk,)))


def RemoveListTowatchList(request , pk):
    if request.method == "POST":
        userThatOwnsTheWatchList = request.user
        theList = Listing.objects.get(pk=pk)
        theList.ListWatchList.remove(userThatOwnsTheWatchList)
        theList.save()
        return  redirect(reverse("DisplayList" ,args=(pk,)))
    
def WatchList(request):
    listingsD = Listing.objects.filter(ListWatchList=request.user)
    return render(request,  'auctions/watchList.html', {'listingsD':listingsD})

def AddBid(request,pk):
    if request.method == 'POST':
        BidOwner = request.user
        ListId= request.POST.get('ListId')
        ListInstance = Listing.objects.get(pk=ListId)
        bid = request.POST.get('BidAmount')
        newBid = Bid(BidUser=BidOwner,
                     bidAmount=bid,
                     BidOnThisList=ListInstance,)
        newBid.save()
        return redirect(reverse("DisplayList" ,args=(pk,)))
    return redirect(reverse("DisplayList" ,args=(pk,)))

def AddComment(request,pk):
    if request.method == 'POST':
        CommentOwnerq = request.user
        Commentq = request.POST.get('Comment')
        commentOnListq = request.POST.get('CommentOnList')
        listinstans = Listing.objects.get(pk=commentOnListq)
        newComment = comments(Comment=Commentq,
                              owner=CommentOwnerq,
                              onList=listinstans)
        newComment.save()
        return redirect(reverse("DisplayList" ,args=(pk,)))

    return render(request, "auctions/index.html")

def unactive(request,ok):
    if request.method == 'POST':
        request.
    
    return  render(request, "auctions/DisplayList.html")

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