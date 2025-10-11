from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('perfil/', views.perfil_view, name='perfil'),

    path('gerenciar/', views.listar_usuarios, name='listar_usuarios'),
    path('gerenciar/criar/', views.criar_usuario_admin, name='criar_usuario_admin'),
    path('gerenciar/editar/<int:pk>/', views.editar_usuario_admin, name='editar_usuario_admin'),
    path('gerenciar/deletar/<int:pk>/', views.deletar_usuario, name='deletar_usuario'),
]