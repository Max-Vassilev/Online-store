from django.urls import path
from online_store.core.views import *

urlpatterns = [
    path("", BasePageView.as_view(), name="base page"),

]