from django.db import models

# Create your models here.
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
    genero = models.CharField(max_length=20, null=False)
    titulo = models.CharField(max_length=50, null=False)
    id_autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    paginas = models.IntegerField(null=False)
    copias = models.IntegerField(null=False)
    
    def __str__(self):
        return self.titulo

class Lector(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    rut = models.IntegerField(null=False, unique=True)
    digito_verificador = models.CharField(max_length=1, null=False)
    correo = models.CharField(max_length=70, blank=True)
    telefono = models.CharField(max_length=12, blank=True)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

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
