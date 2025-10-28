from django.db import models

# Create your models here.
class TipoEmpresas(models.Model):
    id_tipo_empresa = models.AutoField(primary_key=True)
    estado_tipo_empresa = models.SmallIntegerField(unique=True)
    nombre_tipo_empresa = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'tipo_empresas'