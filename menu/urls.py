from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),  # Негизги менюга шилтеме
    path('cakes/', views.cake_list, name='cake_list'),  # Торттордун тизмеси
    path('coffees/', views.coffee_list, name='coffee_list'),  # Кофенин тизмеси
    path('drinks/', views.drink_list, name='drink_list'),  # Суусундуктар
]
