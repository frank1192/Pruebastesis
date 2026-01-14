from rest_framework import serializers
from .models import (
    Estado, Area, Sede, Campus, RolSistema, AreaFuncional,
    TipoPrestamo, EstadoPrestamo, CategoriaImplemento, TipoActividad,
    TipoSolicitud, EstadoSolicitud, TipoMovimiento, TipoSeleccionado,
    RangoDeportivo, UnidadMedida
)


class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'


class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'


class CampusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campus
        fields = '__all__'


class RolSistemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolSistema
        fields = '__all__'


class AreaFuncionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaFuncional
        fields = '__all__'


class TipoPrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoPrestamo
        fields = '__all__'


class EstadoPrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPrestamo
        fields = '__all__'


class CategoriaImplementoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaImplemento
        fields = '__all__'


class TipoActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoActividad
        fields = '__all__'


class TipoSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSolicitud
        fields = '__all__'


class EstadoSolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoSolicitud
        fields = '__all__'


class TipoMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoMovimiento
        fields = '__all__'


class TipoSeleccionadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSeleccionado
        fields = '__all__'


class RangoDeportivoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RangoDeportivo
        fields = '__all__'


class UnidadMedidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnidadMedida
        fields = '__all__'
