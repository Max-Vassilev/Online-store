from django.urls import path
from online_store.core.views import BasePageView

urlpatterns = [
    path("", BasePageView.as_view(), name="base page"),
    path("<str:category>/", BasePageView.as_view(), name="category page"),
]
