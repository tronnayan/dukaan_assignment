from django.urls import path

from .views import OrderView, ProductView, StoreDetailView, StoreView

urlpatterns = [
    path("store",StoreView.as_view()),
    path("product",ProductView.as_view()),
    path("store/<str:store_name>",StoreDetailView.as_view()),
    path("store/<str:store_name>/order",OrderView.as_view())

]
