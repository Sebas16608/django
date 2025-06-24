from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


#categoria
class Category(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(blank=False, null=False)
    slug = models.SlugField(unique=True, max_length=40)
    featured = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

#articulo
class Article(models.Model):
    title = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    image = models.ImageField()
    body = models.TextField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

#Clasificaciones
class Rating(models.Model):
    value = models.FloatField()
    description = models.CharField(max_length=255)
    articl_id = models.ForeignKey(Article, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user_id.username
    
    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'

#Perfil
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profession = models.CharField(max_length=100)
    birthday = models.DateField(null=True)
    about = models.TextField(null=True)
    likedin = models.URLField(max_length=255)
    twitter = models.URLField(max_length=255)
    facebook = models.URLField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'