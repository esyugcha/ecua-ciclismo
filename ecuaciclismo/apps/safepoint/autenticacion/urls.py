from django.urls import path

from . import views

urlpatterns = [
    path('registro', views.RegistroView.as_view(), name='registro'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    
    path('obtener_tokens_administrador', views.ObtenerTokensNotificacionAdministrador.as_view(), name='listado_tokens_administrador'),
]
