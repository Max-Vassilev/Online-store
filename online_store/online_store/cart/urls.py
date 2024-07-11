from django.urls import path
from . import views

urlpatterns = [
    path("", views.cart_summary, name="summary"),
    path("add/", views.add, name="add"),
]
