from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_atendimentos, name='lista_atendimentos'),
    path('cadastro/', views.cadastro_atendimento, name='cadastro_atendimento'),
    path('<int:pk>/', views.detalhes_atendimento, name='detalhes_atendimento'),
]