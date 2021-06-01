from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Finn', views.Finn, name='Finn'),
    path('Jake', views.Jake, name='Jake'),
    path('Marceline', views.Marceline, name='Marceline'),
    path('Princesacaroco', views.Princesacaroco, name='Princesacaroco'),
    path('Princesajujuba', views.Princesajujuba, name='Princesajujuba'),
    path('Princesadefogo', views.Princesadefogo, name='Princesadefogo'),
    path('BMO', views.BMO, name='BMO'),
    path('Ladyiris', views.Ladyiris, name='Ladyiris'),
    path('Reigelado', views.Reigelado, name='Reigelado'),
    path('Lich', views.Lich, name='Lich'),
]

