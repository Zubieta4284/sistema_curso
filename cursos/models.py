from django.db import models
from usuarios.models import Usuario, Estudiante

# Create your models here.
class Curso(models.Model):
  nombre=models.CharField(max_length=100)
  descripcion=models.TextField(blank=True)
  fecha_inicio=models.DateField()
  fecha_fin=models.DateField()
  #relacion uno a muchos, un profesor puede dictar muchos cursos y un curso es dictado por un profesor
  profesor=models.ForeignKey(Usuario, on_delete=models.CASCADE,limit_choices_to={'rol':'profesor'},related_name='cursos_dictados')
  def __str__(self):
    return f"{self.nombre} -{self.fecha_inicio}"
class Inscripcion(models.Model):
    #un estduiante puede inscribirse a muchos cursos y un curso puede tener muchos estudiantes
    estudiante=models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol':'estudiante'},related_name='inscripciones')
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_inscripcion=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return f"{self.estudiante.ci} -inscrito en el curso: {self.curso.nombre}"
    
