from django.db import models
from cursos.models import Inscripcion

# Create your models here.
class Nota(models.Model):
    inscripcion=models.OneToOneField(Inscripcion, on_delete=models.CASCADE)
    nota1=models.DecimalField(max_digits=5, decimal_places=2)
    nota2=models.DecimalField(max_digits=5, decimal_places=2)
    nota_final=models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    aprobado=models.BooleanField(default=False)
    def calcular_nota_final(self):
        if self.nota1 and self.nota2:
            self.nota_final = (self.nota1 + self.nota2) / 2
            self.aprobado = self.nota_final >= 60
            self.save() #porque usar save() para guardar los cambios en la base de datos
        else:
            raise ValueError("Las notas no pueden ser nulas")
    def __str__(self):
        return f"Notas de {self.inscripcion.estudiante.username} - Curso: {self.inscripcion.curso.nombre}"