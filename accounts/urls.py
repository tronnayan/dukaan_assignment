from django.urls import path
from .views import SellerView, CustomerCreateView

urlpatterns = [
    path("seller",SellerView.as_view()),
    path("register-customer",CustomerCreateView.as_view())
]
