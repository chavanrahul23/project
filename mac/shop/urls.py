from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="ShopHome"),
    path("search/", views.search, name="Search"),
    path("products/<int:myid>", views.productView, name="ProductView"),
    path("checkout/", views.checkout, name="checkout"),
]



