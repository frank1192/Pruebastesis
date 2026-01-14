from django.db import models


class Estado(models.Model):
    """Estado - Base table for status"""
    nombre = models.CharField(max_length=256)

    class Meta:
        db_table = 'estado'
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        return self.nombre


class Area(models.Model):
    """Area - Base table for areas"""
    nombre = models.CharField(max_length=256)
    campus = models.CharField(max_length=256)

    class Meta:
        db_table = 'area'
        verbose_name = 'Área'
        verbose_name_plural = 'Áreas'

    def __str__(self):
        return self.nombre


class Sede(models.Model):
    """Sede - Base table for campuses"""
    nombre = models.CharField(max_length=256)

    class Meta:
        db_table = 'sede'
        verbose_name = 'Sede'
        verbose_name_plural = 'Sedes'

    def __str__(self):
        return self.nombre


class Campus(models.Model):
    """Campus - Base table for campus"""
    nombre = models.CharField(max_length=256)
    sede = models.CharField(max_length=256)

    class Meta:
        db_table = 'campus'
        verbose_name = 'Campus'
        verbose_name_plural = 'Campus'

    def __str__(self):
        return self.nombre


class RolSistema(models.Model):
    """Rol_Sistema - Base table for system roles"""
    nombre = models.CharField(max_length=256)
    estado = models.CharField(max_length=256)
    permisos = models.CharField(max_length=256)

    class Meta:
        db_table = 'rol_sistema'
        verbose_name = 'Rol del Sistema'
        verbose_name_plural = 'Roles del Sistema'

    def __str__(self):
        return self.nombre


class AreaFuncional(models.Model):
    """Area_Funcional - Base table for functional areas"""
    nombre = models.CharField(max_length=256)
    estado = models.CharField(max_length=256)
    campus_id = models.CharField(max_length=256)

    class Meta:
        db_table = 'area_funcional'
        verbose_name = 'Área Funcional'
        verbose_name_plural = 'Áreas Funcionales'

    def __str__(self):
        return self.nombre


class TipoPrestamo(models.Model):
    """Tipo_Prestamo - Base table for loan types"""
    nombre = models.CharField(max_length=256)

    class Meta:
        db_table = 'tipo_prestamo'
        verbose_name = 'Tipo de Préstamo'
        verbose_name_plural = 'Tipos de Préstamo'

    def __str__(self):
        return self.nombre


class EstadoPrestamo(models.Model):
    """Estado_Prestamo - Base table for loan status"""
    nombre = models.CharField(max_length=256)

    class Meta:
        db_table = 'estado_prestamo'
        verbose_name = 'Estado de Préstamo'
        verbose_name_plural = 'Estados de Préstamo'

    def __str__(self):
        return self.nombre


class CategoriaImplemento(models.Model):
    """Categoria_Implemento - Base table for equipment categories"""
    nombre = models.CharField(max_length=256)

    class Meta:
        db_table = 'categoria_implemento'
        verbose_name = 'Categoría de Implemento'
        verbose_name_plural = 'Categorías de Implemento'

    def __str__(self):
        return self.nombre


class TipoActividad(models.Model):
    """Tipo_Actividad - Base table for activity types"""
    nombre = models.CharField(max_length=256)

    class Meta:
        db_table = 'tipo_actividad'
        verbose_name = 'Tipo de Actividad'
        verbose_name_plural = 'Tipos de Actividad'

    def __str__(self):
        return self.nombre


class TipoSolicitud(models.Model):
    """Tipo_Solicitud - Base table for request types"""
    nombre = models.CharField(max_length=256)

    class Meta:
        db_table = 'tipo_solicitud'
        verbose_name = 'Tipo de Solicitud'
        verbose_name_plural = 'Tipos de Solicitud'

    def __str__(self):
        return self.nombre


class EstadoSolicitud(models.Model):
    """Estado_Solicitud - Base table for request status"""
    nombre = models.CharField(max_length=256)

    class Meta:
        db_table = 'estado_solicitud'
        verbose_name = 'Estado de Solicitud'
        verbose_name_plural = 'Estados de Solicitud'

    def __str__(self):
        return self.nombre


class TipoMovimiento(models.Model):
    """Tipo_Movimiento - Base table for movement types"""
    nombre = models.CharField(max_length=256)

    class Meta:
        db_table = 'tipo_movimiento'
        verbose_name = 'Tipo de Movimiento'
        verbose_name_plural = 'Tipos de Movimiento'

    def __str__(self):
        return self.nombre


class TipoSeleccionado(models.Model):
    """Tipo_Seleccionado - Base table for selection types"""
    nombre = models.CharField(max_length=256)

    class Meta:
        db_table = 'tipo_seleccionado'
        verbose_name = 'Tipo Seleccionado'
        verbose_name_plural = 'Tipos Seleccionados'

    def __str__(self):
        return self.nombre


class RangoDeportivo(models.Model):
    """Rango_Deportivo - Base table for sports ranges"""
    nombre = models.CharField(max_length=256)

    class Meta:
        db_table = 'rango_deportivo'
        verbose_name = 'Rango Deportivo'
        verbose_name_plural = 'Rangos Deportivos'

    def __str__(self):
        return self.nombre


class UnidadMedida(models.Model):
    """Unidad_Medida - Base table for measurement units"""
    nombre = models.CharField(max_length=256)

    class Meta:
        db_table = 'unidad_medida'
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medida'

    def __str__(self):
        return self.nombre

