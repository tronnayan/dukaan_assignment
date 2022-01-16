from django.urls import path
from .views import SellerView

urlpatterns = [
    path("seller",SellerView.as_view()),
]
