from django.db import models
from django.utils import timezone
# Create your models here.
class Comuna(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad_habitantes = models.IntegerField(null=True)
    tasa_de_vulnerabilidad = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    fecha_de_fundacion = models.DateField(default=timezone.now)