from django.contrib import admin
from .models import Post

# Register your models here.

# register the model for a blog post we created as a class in the models.py file
admin.site.register(Post)
