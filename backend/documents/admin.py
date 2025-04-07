from django.contrib import admin
from .models import Empleado, Documento

admin.site.site_header = "Panel de Control de Legalidad"
admin.site.site_title = "Sistema Legalidad"
admin.site.index_title = "Administración de Documentos y Empleados"


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'empresa', 'documentos_pendientes')
    search_fields = ('nombre', 'empresa')

    def documentos_pendientes(self, obj):
        return obj.documentos.filter(validado=False).count()
    documentos_pendientes.short_description = 'Pendientes'


@admin.register(Documento)
class DocumentoAdmin(admin.ModelAdmin):
    list_display = ('empleado', 'tipo', 'fecha_vencimiento', 'esta_vencido', 'validado')
    list_filter = ('validado', 'tipo', 'empleado__empresa')
    date_hierarchy = 'fecha_vencimiento'
    actions = ['marcar_como_validado']

    def esta_vencido(self, obj):
        from django.utils import timezone
        return obj.fecha_vencimiento < timezone.now().date()
    esta_vencido.boolean = True
    esta_vencido.short_description = 'Vencido'

    def marcar_como_validado(self, request, queryset):
        queryset.update(validado=True)
    marcar_como_validado.short_description = "Marcar como validado"
