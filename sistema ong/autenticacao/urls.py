from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('usuarios/', views.lista_usuarios, name='lista_usuarios'),
    path('usuarios/cadastro/', views.cadastro_usuario, name='cadastro_usuario'),
    path('usuarios/<int:pk>/', views.detalhes_usuario, name='detalhes_usuario'),
]