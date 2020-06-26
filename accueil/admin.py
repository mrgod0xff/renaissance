from django.contrib import admin

# Register your models here.
from .models import Vision, Strategie, Carousel, Priorite, Objectif, Biographie, Event


admin.site.register(Biographie)
admin.site.register(Carousel)
admin.site.register(Event)
admin.site.register(Objectif)
admin.site.register(Vision)
admin.site.register(Priorite)
admin.site.register(Strategie)