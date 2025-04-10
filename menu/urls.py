from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_view, name='menu'),  # Негизги менюга шилтеме
    path('cakes/', views.cake_list, name='cake_list'),  # Торттордун тизмеси
    path('coffees/', views.coffee_list, name='coffee_list'),  # Кофенин тизмеси
    path('drinks/', views.drink_list, name='drink_list'),  # Суусундуктар
]
# menu/urls.py
from django.urls import path
from . import views # Эгер views импорттолгон болсо, кайра жазуунун кереги жок

urlpatterns = [
    path('', views.menu_view, name='menu'), # Башкы бет
    path('cakes/', views.cake_list, name='cake_list'),
    path('coffees/', views.coffee_list, name='coffee_list'),
    path('drinks/', views.drink_list, name='drink_list'),

    # ----- ЖАҢЫ ЖОЛДУ КОШУҢУЗ: -----
    path('contact/', views.contact_view, name='contact_page'),
    # --------------------------------
]