from django.urls import path
from . import views

urlpatterns = [
    # — Español —
    path('', views.inicio, name='inicio'),
    path('acerca/', views.acerca, name='acerca'),
    path('recursos/', views.recursos_view, name='recursos'),
    path('contacto/', views.contacto, name='contacto'),
    # — English —
    path('en/', views.inicio_en, name='inicio_en'),
    path('en/about/', views.about_en, name='acerca_en'),
    path('en/resources/', views.resources_en, name='recursos_en'),
    path('en/contact/', views.contact_en, name='contacto_en'),
]
