from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    EstadoViewSet, AreaViewSet, SedeViewSet, CampusViewSet,
    RolSistemaViewSet, AreaFuncionalViewSet, TipoPrestamoViewSet,
    EstadoPrestamoViewSet, CategoriaImplementoViewSet, TipoActividadViewSet,
    TipoSolicitudViewSet, EstadoSolicitudViewSet, TipoMovimientoViewSet,
    TipoSeleccionadoViewSet, RangoDeportivoViewSet, UnidadMedidaViewSet
)

router = DefaultRouter()
router.register(r'estados', EstadoViewSet)
router.register(r'areas', AreaViewSet)
router.register(r'sedes', SedeViewSet)
router.register(r'campus', CampusViewSet)
router.register(r'roles-sistema', RolSistemaViewSet)
router.register(r'areas-funcionales', AreaFuncionalViewSet)
router.register(r'tipos-prestamo', TipoPrestamoViewSet)
router.register(r'estados-prestamo', EstadoPrestamoViewSet)
router.register(r'categorias-implemento', CategoriaImplementoViewSet)
router.register(r'tipos-actividad', TipoActividadViewSet)
router.register(r'tipos-solicitud', TipoSolicitudViewSet)
router.register(r'estados-solicitud', EstadoSolicitudViewSet)
router.register(r'tipos-movimiento', TipoMovimientoViewSet)
router.register(r'tipos-seleccionado', TipoSeleccionadoViewSet)
router.register(r'rangos-deportivos', RangoDeportivoViewSet)
router.register(r'unidades-medida', UnidadMedidaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
