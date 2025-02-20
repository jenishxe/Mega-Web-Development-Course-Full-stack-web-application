from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('products/<product>/', views.products, name="products"),
    path('products/<product_brand>/<product_slug>/', views.product_page, name="product_page"),
    path('signup/', views.signup, name = "signup"),
]