from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    empresa = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} ({self.empresa})"

class Documento(models.Model):
    TIPOS_DOC = [
        ('EPP', 'Equipo de Protección'),
        ('REC', 'Recibo de Sueldo'),
        ('ANT', 'Antecedentes Penales'),
    ]
    
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='documentos')
    tipo = models.CharField(max_length=3, choices=TIPOS_DOC)
    archivo = models.FileField(upload_to='documentos/')
    fecha_vencimiento = models.DateField()
    validado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.get_tipo_display()} - {self.empleado.nombre}"