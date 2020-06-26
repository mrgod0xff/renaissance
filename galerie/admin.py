from django.contrib import admin

# Register your models here.
from .models import Image_long, Image_large


admin.site.register(Image_large)
admin.site.register(Image_long)