from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('CreatList', views.CreatList, name="CreatList"),
    path('DisplayList/<int:pk>', views.DisplayList, name="DisplayList"), # type: ignore
    path('AddListTowatchList/<int:pk>', views.AddListTowatchList,name='AddListTowatchList'), # type: ignore
    path('RemoveListTowatchList/<int:pk>',views.RemoveListTowatchList,name = 'RemoveListTowatchList'), # type: ignore
    path('WatchList', views.WatchList , name='WatchList'),
    path('AddBid', views.AddBid, name="AddBid"),
]