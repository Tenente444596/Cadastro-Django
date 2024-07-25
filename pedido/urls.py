from django.urls import path
from . import views

urlpatterns = [
    path("validaCupom/", views.validaCupom, name='validaCupom'),
    path("finalizar_pedido/", views.finalizar_pedido, name='finalizar_pedido'),
]