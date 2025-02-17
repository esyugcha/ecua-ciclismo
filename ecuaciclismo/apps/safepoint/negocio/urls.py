from django.urls import path

from . import views

urlpatterns = [
    path('obtener_actualizar', views.ObtenerDetalleActualizarNegocioView.as_view(), name='obtener_actualizar_negocio'),
    path('obtener_solicitud', views.ObtenerEstadoSolicitudNegocioView.as_view(), name='solicitud_negocio'),
    path('generar_solicitud', views.CrearSolicitudNegocioView.as_view(), name='generar_solicitud'),
    path('obtener_estado', views.ObtenerEstadoVisibilidadNegocio.as_view(), name='obtener_estado_activo'),
    
    path('productos', views.ProductoListaView.as_view(), name='listado_productos_local'),    
    path('servicios', views.ServicioLocalListaView.as_view(), name='listado_servicios'),
    path('servicios_adicionales', views.ServiciosAdicionalesListaView.as_view(), name='listado_servicios_adicionales_local'),
    
    path('obtener_estadisticas', views.EstadisticaNegocioView.as_view(), name="obtener_estadisticas"),
    path("actualizar_estadistica", views.ActualizarEstadisticasPorCiclistaView.as_view(), name="actualizar_estadistica"),
    
    path("registrar_aviso", views.RegistrarAvisosNegocioView.as_view(), name="registrar_aviso"),
    path('todos_negocios', views.ObtenerTodosNegociosView.as_view(), name='todos_negocios'),

    # path('actualizar/<int:pk>', views.UpdateNegocioView.as_view(), name='obtener_actualizar_negocio'),    
]
