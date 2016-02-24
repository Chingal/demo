from django.db import models
from django.contrib.auth.models import User

TIPO_USUARIO = (
   ('invitado', 'Invitado'),
   ('admin', 'Admin'),
)

class userProfile(models.Model):
    #Ruta de la Imagen
    def post(self, request, *args, **kwargs):
        pass

    def rutaImagen(self,filename):
        ruta = "UserProfile/%s/%s/" % (self.user.username, str(filename))
        return ruta

    #Atributos
    user        = models.OneToOneField(User)
    foto        = models.ImageField(upload_to=rutaImagen)
    telefono    = models.CharField(max_length=100)
    tipo        = models.CharField(max_length=100, choices=TIPO_USUARIO)

    class Meta:
        verbose_name = ('User Profile')
        verbose_name_plural = ('Users Profiles')

    def __unicode__(self):
        return self.user.username