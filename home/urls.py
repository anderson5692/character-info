from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:personagem_Nome>', views.info_personagem, name='info'),
]