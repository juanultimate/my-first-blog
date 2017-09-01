from django.contrib import admin
from .models import Post

#registrar el modelo en la base de datos.
admin.site.register(Post)
