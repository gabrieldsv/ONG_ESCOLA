from django.urls import path
from . import views

urlpatterns = [
    path('frequencia/', views.relatorio_frequencia, name='relatorio_frequencia'),
    path('cursos/', views.relatorio_cursos, name='relatorio_cursos'),
    path('certificados/', views.relatorio_certificados, name='relatorio_certificados'),
]