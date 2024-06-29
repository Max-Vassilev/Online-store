from django.urls import path
from online_store.core.views import *

urlpatterns = [
    path('about/', AboutPageView.as_view(), name="about"),
    path('contacts/', ContactsPageView.as_view(), name="contacts"),
    path("", BasePageView.as_view(), name="base page"),
    path("<str:category>/", BasePageView.as_view(), name="category page"),
]
