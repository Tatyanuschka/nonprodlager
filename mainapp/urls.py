from django.urls import path
from mainapp import views
from mainapp.apps import MainappConfig



app_name = MainappConfig.name

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('request/', views.RequestView.as_view()),
    path('response/', views.ResponseView.as_view()),
]
