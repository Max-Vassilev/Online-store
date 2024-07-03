from django.urls import path
from . import views

urlpatterns = [
    path("", views.BasePageView.as_view(), name="base_page"),
    path('category/<str:category>/', views.BasePageView.as_view(), name="category_page"),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name="product_detail"),
    path('about/', views.AboutPageView.as_view(), name="about"),
    path('contacts/', views.ContactsPageView.as_view(), name="contacts"),
    path('category/<str:category>/', views.BasePageView.as_view(), name="category_page"),
]
