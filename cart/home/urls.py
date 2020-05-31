from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="HOME"),
    path('register', views.register, name="REGISTER"),
    path('login', views.login, name="LOGIN"),
    path('registerAccount', views.registerAccount, name="REGISTER"),
    path('log', views.loginto, name="LOGIN"),
    path('logout', views.logout, name="LOGOUT"),
    path('search', views.searchITem, name="SEARCH"),
    path('items', views.itemList.as_view(), name="ITEM"),
    path('items/<int:pk>', views.itemList.as_view(), name="ITEM")
]
