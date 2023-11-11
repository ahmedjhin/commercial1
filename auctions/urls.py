from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('CreatList', views.CreatList, name="CreatList"),
    path('DisplayList/<int:pk>', views.DisplayList, name="DisplayList"), 
    path('AddListTowatchList/<int:pk>', views.AddListTowatchList,name='AddListTowatchList'), # type: ignore
    path('RemoveListTowatchList/<int:pk>',views.RemoveListTowatchList,name = 'RemoveListTowatchList'), # type: ignore
    path('WatchList', views.WatchList , name='WatchList'),
    path('AddBid/<int:pk>', views.AddBid, name="AddBid"),
    path('AddComment/<int:pk>', views.AddComment, name="AddComment"),
    path('unactive/<int:pk>', views.unactive, name="unactive"),
]