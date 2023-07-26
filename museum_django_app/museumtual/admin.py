from django.contrib import admin
from .models import Museumtual
from .models import Type
from .models import Book
from .models import Cart
from .models import Museum

# Register your models here.

admin.site.register(Museumtual)
admin.site.register(Type)
admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(Museum)


