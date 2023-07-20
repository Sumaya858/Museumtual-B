from django.contrib import admin
from .models import Museumtual
from .models import Type
from .models import Profile
from .models import Cart

# Register your models here.

admin.site.register(Museumtual)
admin.site.register(Type)
admin.site.register(Profile)
admin.site.register(Cart)


