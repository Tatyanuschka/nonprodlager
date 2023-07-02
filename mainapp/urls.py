from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig



app_name = MainappConfig.name

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('about/', views.AboutView.as_view()),
    path('contact/', views.ContactView.as_view()),
    path('products/', views.ProductsView.as_view()),
    path('productdetail/', views.ProductDetailView.as_view()),
    path('shoppingcart/', views.ShoppingCartView.as_view()),
]
