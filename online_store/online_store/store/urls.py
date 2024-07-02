from django.urls import path
from .views import BasePageView, AboutPageView, ContactsPageView

urlpatterns = [
    path("", BasePageView.as_view(), name="base_page"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('contacts/', ContactsPageView.as_view(), name="contacts"),
    path('category/<str:category>/', BasePageView.as_view(), name="category_page"),
]
