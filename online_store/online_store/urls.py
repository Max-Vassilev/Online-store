from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('online_store.core.urls')),
    path('cart/', include('online_store.cart.urls')),
]