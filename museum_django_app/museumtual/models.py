# from os import path, environ
from django.db import models
from token_auth.models import User

# from django.contrib.auth.models import User




# Models Profile


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    

# Cart
class Cart(models.Model):

    MUSEUM_CHOICES = [
        (' ', " "),
        ('acropolis', "Acropolis"),
        ('egypt', "Egypt"),

    ]
    museum_choice = models.CharField(max_length=100, choices=MUSEUM_CHOICES, default='other')
    # name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=50, decimal_places=2) 

    def __str__(self):
        return f'{self.name.price} Cart' 
    
# Create your models here.

class Type(models.Model):
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name


class Museumtual(models.Model):
    name = models.CharField(max_length=100)
    origin = models.CharField(max_length=100)
    image = models.CharField(max_length=400)
    type = models.ManyToManyField(Type, related_name='type', blank=True )
    owner = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} from {self.origin}'
