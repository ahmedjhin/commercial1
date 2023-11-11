from .models import User , Listing

def watchListItems(request):
    current_user = request.user if request.user.is_authenticated else None
    x = Listing.objects.filter(ListWatchList=current_user)
    d = str(len(x))
    return {'d':d}
