from django.urls import path
from . import views

urlpatterns = [
    path('equipes/', views.time_list, name='equipe_list'),
    path('equipes/create/', views.time_create, name='equipe_create'),
    path('equipes/update/<int:id>/', views.time_update, name='equipe_update'),
    path('equipes/delete/<int:id>/', views.time_delete, name='equipe_delete'),

    path('jogadores/', views.jogador_list, name='jogador_list'),
    path('jogadores/create/', views.jogador_create, name='jogador_create'),
    path('jogadores/update/<int:id>/', views.jogador_update, name='jogador_update'),
    path('jogadores/delete/<int:id>/', views.jogador_delete, name='jogador_delete'),
]
