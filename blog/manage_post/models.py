from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()  # Obtiene el modelo de usuario activo (por si usas User personalizado)

# Modelo que representa las categorías para los artículos
class Category(models.Model):
    name = models.CharField(max_length=20)  # Nombre de la categoría, texto corto máximo 20 caracteres
    image = models.ImageField(upload_to='Categories', blank=False, null=False)  # Imagen representativa, obligatorio subir una imagen
    slug = models.SlugField(unique=True, max_length=40)  # Texto amigable para URLs, debe ser único
    featured = models.BooleanField(default=False)  # Indica si la categoría está destacada o no
    created = models.DateTimeField(auto_now_add=True)  # Fecha y hora en que se creó la categoría (se añade automáticamente)
    update = models.DateTimeField(auto_now=True)  # Fecha y hora de la última actualización (se actualiza automáticamente)
    status = models.BooleanField(default=True)  # Indica si la categoría está activa (True) o inactiva (False)

    def __str__(self):
        # Método especial para mostrar el nombre de la categoría cuando se imprime o en el admin
        return self.name
    
    class Meta:
        # Meta sirve para configurar nombres legibles para el modelo en singular y plural
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

# Modelo que representa los artículos o posts
class Article(models.Model):
    title = models.CharField(max_length=255)  # Título del artículo, texto corto
    introduction = models.CharField(max_length=255)  # Introducción o resumen del artículo
    slug = models.SlugField(unique=True, max_length=255)  # URL amigable única para identificar el artículo
    image = models.ImageField(upload_to='Articles', blank=False, null=False)  # Imagen principal del artículo
    body = models.TextField()  # Contenido completo del artículo, texto largo sin límite
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  
    # Relación muchos a uno con el usuario que escribió el artículo
    # on_delete=models.CASCADE significa que si el usuario se borra, sus artículos también
    categories = models.ManyToManyField(Category)  
    # Relación muchos a muchos con categorías, un artículo puede pertenecer a varias categorías
    created = models.DateTimeField(auto_now_add=True)  # Fecha y hora de creación automática
    update = models.DateTimeField(auto_now=True)  # Fecha y hora de la última actualización automática
    status = models.BooleanField(default=True)  # Estado activo/inactivo del artículo

    def __str__(self):
        # Muestra el título cuando se imprime o en el admin
        return self.title
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

# Modelo para calificaciones o valoraciones de artículos
class Rating(models.Model):
    value = models.FloatField()  # Valor numérico de la calificación (puede tener decimales)
    description = models.CharField(max_length=255)  # Comentario o descripción de la calificación
    articl_id = models.ForeignKey(Article, on_delete=models.CASCADE)  
    # Relación muchos a uno con el artículo calificado
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)  
    # Relación muchos a uno con el usuario que hizo la calificación
    status = models.BooleanField(default=True)  # Estado activo/inactivo de la calificación

    def __str__(self):
        # Muestra el nombre del usuario que calificó cuando se imprime o en el admin
        return self.user_id.username
    
    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

#Perfil

class Profile(models.Model):
    profession = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    about = models.TextField(null=True)
    likedin = models.URLField(max_length=255)
    twitter = models.URLField(max_length=255)
    facebook = models.URLField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'