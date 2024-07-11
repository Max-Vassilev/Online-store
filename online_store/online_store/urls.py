from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('online_store.store.urls')),
    path('cart/', include('online_store.cart.urls'))
]