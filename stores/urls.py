from django.urls import path

from .views import ProductView, StoreView

urlpatterns = [
    path("store",StoreView.as_view()),
    path("product",ProductView.as_view())

]
