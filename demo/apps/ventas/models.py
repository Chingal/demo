from django.db import models

class Cliente(models.Model):
    #Atributos del CLiente
    nombres   = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    status    = models.BooleanField(default=True)

    class Meta:
        verbose_name = ('Cliente')
        verbose_name_plural = ('Clientes')

    def __unicode__(self):
        return ("%s %s") % (self.nombres, self.apellidos)

class Producto(models.Model):
    #Atributos del Producto
    nombre      = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=300)
    status      = models.BooleanField(default=True)

    class Meta:
        verbose_name = ('Producto')
        verbose_name_plural = ('Productos')

    def __unicode__(self):
        return self.nombre
