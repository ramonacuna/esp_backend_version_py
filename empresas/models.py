from django.db import models

# Create your models here.
class Empresas(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    direccion_empresa = models.CharField(unique=True, max_length=200)
    nombre_empresa = models.CharField(unique=True, max_length=200)
    telefono_empresa = models.CharField(unique=True, max_length=200)
    id_tipo_empresa = models.ForeignKey(
        'tipos_empresas.TipoEmpresas', 
        on_delete=models.PROTECT,
        db_column='id_tipo_empresa'
    )

    class Meta:
        managed = False
        db_table = 'empresas'
