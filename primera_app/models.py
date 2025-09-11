from django.db import models

# Create your models here.
class Nacionalidad(models.Model):
    pais = models.CharField(max_length=56,null=False)
    Nacionalidad = models.CharField(max_length=56,null=False)

class Autor(models.Model):
    nombre = models.CharField(max_length=250,null=False)
    pseudonimo = models.CharField(max_length=50,null=True)
    id_nacionalidad = models.ForeignKey(Nacionalidad,on_delete=models.CASCADE)
    bio = models.TextField()

class Comuna(models.Model):
    codigo = models.CharField(max_length=5,null=False)
    comuna = models.CharField(max_length=50,null=False)

class  Direccion(models.Model):
    id_comuna = models.ForeignKey(Comuna, on_delete=models.CASCADE)
    calle = models.CharField(max_length=50, null=True)
    numero = models.CharField(max_length=10, null=True)
    departamento = models.CharField(max_length=10 , null=True)

class Biblioteca(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    id_direccion = models.ForeignKey(Direccion,on_delete=models.CASCADE)

class Libro(models.Model):
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete=models.CASCADE)
    genero = models.CharField(max_length=20, null= False)
    titulo = models.CharField(max_length=50, null= False)
    id_autor = models.ForeignKey(Autor,on_delete= models.CASCADE)
    paginas = models.IntegerField( null= False)
    copias = models.IntegerField( null= False)

class Lector(models.Model):
    nombre = models.CharField(max_length=50, null= False)
    rut = models.IntegerField(null=False, unique=True)
    digito_verificador = models.CharField(max_length=1, null= False)
    correo = models.CharField(max_length=70, null= True)
    telefono = models.CharField(max_length=12, null= True)
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)
    id_biblioteca = models.ForeignKey(Biblioteca, on_delete= models.CASCADE)

class Prestamo(models.Model):
    id_libro = models.ForeignKey(Libro,on_delete=models.CASCADE)
    id_lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField(null= False)
    fecha_devolucion = models.DateField(null= False)

class TipoCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique= True)
    habilitado = models.BooleanField(default= True)
    # AÑADE null=True a estas dos líneas
    updated_at = models.DateTimeField(auto_now = True, null=True)
    created_at = models.DateTimeField(auto_now_add = True, null=True)
    
    def __str__(self):
        return self.nombre 

class Categoria(models.Model):
    tipo_categoria = models.ForeignKey(TipoCategoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    habilitado = models.BooleanField(default=True)
    # AÑADE null=True a estas dos líneas
    updated_at = models.DateTimeField(auto_now=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre
