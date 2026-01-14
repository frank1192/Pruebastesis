from django.contrib import admin
from .models import (
    Estado, Area, Sede, Campus, RolSistema, AreaFuncional,
    TipoPrestamo, EstadoPrestamo, CategoriaImplemento, TipoActividad,
    TipoSolicitud, EstadoSolicitud, TipoMovimiento, TipoSeleccionado,
    RangoDeportivo, UnidadMedida
)


@admin.register(Estado)
class EstadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']


@admin.register(Area)
class AreaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'campus']
    search_fields = ['nombre', 'campus']


@admin.register(Sede)
class SedeAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'sede']
    search_fields = ['nombre', 'sede']


@admin.register(RolSistema)
class RolSistemaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'estado']
    search_fields = ['nombre']


@admin.register(AreaFuncional)
class AreaFuncionalAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'estado', 'campus_id']
    search_fields = ['nombre']


@admin.register(TipoPrestamo)
class TipoPrestamoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']


@admin.register(EstadoPrestamo)
class EstadoPrestamoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']


@admin.register(CategoriaImplemento)
class CategoriaImplementoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']


@admin.register(TipoActividad)
class TipoActividadAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']


@admin.register(TipoSolicitud)
class TipoSolicitudAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']


@admin.register(EstadoSolicitud)
class EstadoSolicitudAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']


@admin.register(TipoMovimiento)
class TipoMovimientoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']


@admin.register(TipoSeleccionado)
class TipoSeleccionadoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']


@admin.register(RangoDeportivo)
class RangoDeportivoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']


@admin.register(UnidadMedida)
class UnidadMedidaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre']
    search_fields = ['nombre']

