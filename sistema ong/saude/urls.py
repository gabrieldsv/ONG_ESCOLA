from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_fichas, name='lista_fichas'),
    path('cadastro/', views.cadastro_ficha, name='cadastro_ficha'),
    path('<int:pk>/', views.detalhes_ficha, name='detalhes_ficha'),
]