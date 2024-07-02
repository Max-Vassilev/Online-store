from django.urls import path
from online_store.core.views import *

urlpatterns = [
    path("", BasePageView.as_view(), name="base_page"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('contacts/', ContactsPageView.as_view(), name="contacts"),
]
