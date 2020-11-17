from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'app-home'),
    path('favourites/', views.favourites, name = 'app-favourites'),
    path('simulate/', views.simulate, name = 'app-simulate'),
    path ('search/', views.searchName),

]
