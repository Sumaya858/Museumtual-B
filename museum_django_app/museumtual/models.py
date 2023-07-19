from django.db import models
from token_auth.models import User

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
