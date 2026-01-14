from rest_framework import viewsets
from .models import (
    Estado, Area, Sede, Campus, RolSistema, AreaFuncional,
    TipoPrestamo, EstadoPrestamo, CategoriaImplemento, TipoActividad,
    TipoSolicitud, EstadoSolicitud, TipoMovimiento, TipoSeleccionado,
    RangoDeportivo, UnidadMedida
)
from .serializers import (
    EstadoSerializer, AreaSerializer, SedeSerializer, CampusSerializer,
    RolSistemaSerializer, AreaFuncionalSerializer, TipoPrestamoSerializer,
    EstadoPrestamoSerializer, CategoriaImplementoSerializer, TipoActividadSerializer,
    TipoSolicitudSerializer, EstadoSolicitudSerializer, TipoMovimientoSerializer,
    TipoSeleccionadoSerializer, RangoDeportivoSerializer, UnidadMedidaSerializer
)


class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer


class AreaViewSet(viewsets.ModelViewSet):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer


class SedeViewSet(viewsets.ModelViewSet):
    queryset = Sede.objects.all()
    serializer_class = SedeSerializer


class CampusViewSet(viewsets.ModelViewSet):
    queryset = Campus.objects.all()
    serializer_class = CampusSerializer


class RolSistemaViewSet(viewsets.ModelViewSet):
    queryset = RolSistema.objects.all()
    serializer_class = RolSistemaSerializer


class AreaFuncionalViewSet(viewsets.ModelViewSet):
    queryset = AreaFuncional.objects.all()
    serializer_class = AreaFuncionalSerializer


class TipoPrestamoViewSet(viewsets.ModelViewSet):
    queryset = TipoPrestamo.objects.all()
    serializer_class = TipoPrestamoSerializer


class EstadoPrestamoViewSet(viewsets.ModelViewSet):
    queryset = EstadoPrestamo.objects.all()
    serializer_class = EstadoPrestamoSerializer


class CategoriaImplementoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaImplemento.objects.all()
    serializer_class = CategoriaImplementoSerializer


class TipoActividadViewSet(viewsets.ModelViewSet):
    queryset = TipoActividad.objects.all()
    serializer_class = TipoActividadSerializer


class TipoSolicitudViewSet(viewsets.ModelViewSet):
    queryset = TipoSolicitud.objects.all()
    serializer_class = TipoSolicitudSerializer


class EstadoSolicitudViewSet(viewsets.ModelViewSet):
    queryset = EstadoSolicitud.objects.all()
    serializer_class = EstadoSolicitudSerializer


class TipoMovimientoViewSet(viewsets.ModelViewSet):
    queryset = TipoMovimiento.objects.all()
    serializer_class = TipoMovimientoSerializer


class TipoSeleccionadoViewSet(viewsets.ModelViewSet):
    queryset = TipoSeleccionado.objects.all()
    serializer_class = TipoSeleccionadoSerializer


class RangoDeportivoViewSet(viewsets.ModelViewSet):
    queryset = RangoDeportivo.objects.all()
    serializer_class = RangoDeportivoSerializer


class UnidadMedidaViewSet(viewsets.ModelViewSet):
    queryset = UnidadMedida.objects.all()
    serializer_class = UnidadMedidaSerializer

