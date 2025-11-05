from django.db import models
from rutificador import Rut
from django.core.exceptions import ValidationError
import datetime

ahora = datetime.datetime.now

# Acá creo mis validaciones personalizadas para el RUT y la edad

def validar_rut(rut):
    try:
        rut_valido = Rut(rut)
    except:
        raise ValidationError('Dígito verificador NO corresponde.')


def validar_mayoria_edad(fecha_nacimiento):
    fecha_actual = datetime.datetime.today()
    edad = fecha_actual.year - fecha_nacimiento.year
    if (fecha_nacimiento.month, fecha_nacimiento.day) > (fecha_actual.month, fecha_actual.day):
        edad -= 1
    if edad < 18:
        raise ValidationError('Debe ser mayor de edad...')
# Acá voy creando todos mis modelos para el sistema de biblioteca

class Nacionalidad(models.Model):
    pais = models.CharField(max_length=56,null=False)
    nombre_nacionalidad = models.CharField(max_length=56,null=False)

    class Meta:
        verbose_name_plural = "Nacionalidades"
    def __str__(self):
        return self.nombre_nacionalidad

class Autor(models.Model):
    nombre = models.CharField(max_length=250,null=False)
    pseudonimo = models.CharField(max_length=50,blank=True)
    id_nacionalidad = models.ForeignKey(Nacionalidad,on_delete=models.CASCADE)
    bio = models.TextField()
    
    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    codigo = models.CharField(max_length=5,null=False)
    comuna = models.CharField(max_length=50,null=False)
    
    def __str__(self):
        return self.comuna

class Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    calle = models.CharField(max_length=50, blank=True)
    numero = models.CharField(max_length=10, blank=True)
    departamento = models.CharField(max_length=10, blank=True)
    
    class Meta:
        verbose_name_plural = "Direcciones"
    def __str__(self):
        return f"{self.calle} {self.numero}, {self.id_comuna.comuna}"
    
class Biblioteca(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    id_direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class Libro(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, blank=True, null=True)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    genero = models.CharField(max_length=20, null=False)
    titulo = models.CharField(max_length=50, null=False)
    paginas = models.IntegerField(null=False)
    copias = models.IntegerField(null=False)

    def __str__(self):
        return self.titulo

class Lector(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE, blank=False)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, blank=True)
    rut_lector = models.CharField(max_length=12, blank=False, unique=True, validators=[validar_rut])
    nombre_lector = models.CharField(max_length=255, blank=False)
    correo_lector = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    fecha_nacimiento = models.DateField(blank=True, null=True, validators=[validar_mayoria_edad])
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=ahora)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_lector

class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro,on_delete=models.CASCADE)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(null=False)
    fecha_devolucion = models.DateField(null=False)
    
    def __str__(self):
        return f"{self.id_libro.titulo} - {self.id_lector.nombre}"

class TipoCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    habilitado = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.nombre 

class Categoria(models.Model):
    tipo_categoria = models.ForeignKey(TipoCategoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    habilitado = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre
