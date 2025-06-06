from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class Usuario(AbstractUser):
    ROLES = (
        ('administrador', 'Administrador'), 
        ('profesor', 'Profesor'),
        ('estudiante', 'Estudiante'),
    )
    rol=models.CharField(max_length=20, choices=ROLES, default='estudiante')
    def __str__(self):
        return f"{self.username} - {self.rol}"

class Estudiante(models.Model):
    usuario=models.OneToOneField('usuarios.Usuario', on_delete=models.CASCADE)
    ci=models.CharField(max_length=15, unique=True)
    celular=models.CharField(max_length=15)
    
    def __str__(self):
        return self.ci
    