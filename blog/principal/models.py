from django.db import models

class Autor(models.Model):
	Nombre = models.CharField(max_length=250)

	def __str__(self):
		return self.Nombre

	class Meta:
		verbose_name_plural='Autores'

class Entrada(models.Model):
	Titulo = models.CharField(max_length=250)
	Fecha = models.DateTimeField(auto_now_add=True)
	Contenido = models.TextField()
	Autor = models.ForeignKey(Autor)

	def __str__(self):
		return self.Titulo

	class Meta: 
		verbose_name_plural='Entradas'


class Comentario(models.Model):
    fechacreacion = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=100)
    mensaje = models.TextField()
    identrada = models.ForeignKey(Entrada)

    def __str__(self):
        return str("%s %s " % (self.identrada,self.mensaje[:60]))