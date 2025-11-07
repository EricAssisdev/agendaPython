from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_contatos, name='lista_contatos'),
    path('contato/<int:pk>/', views.detalhes_contato, name='detalhes_contato'),
    path('contato/novo/', views.criar_contato, name='criar_contato'),
    path('contato/<int:pk>/editar/', views.editar_contato, name='editar_contato'),
    path('contato/<int:pk>/deletar/', views.deletar_contato, name='deletar_contato'),
    path('contato/<int:pk>/favorito/', views.toggle_favorito, name='toggle_favorito'),
]
