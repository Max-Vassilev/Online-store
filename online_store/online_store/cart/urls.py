from django.urls import path
from online_store.cart.views import *

urlpatterns = [
    path('', CartSummary.as_view(), name="summary"),
]
