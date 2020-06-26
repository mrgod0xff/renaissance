import os
import uuid
import random

from django.db import models

# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "actualite/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename)

class Categorie(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titre   =  models.CharField(max_length=200)
    image   =  models.ImageField(upload_to=image_path, null=True, blank=True)
    genre   =  models.ForeignKey('Categorie', on_delete=models.CASCADE)
    active  =  models.BooleanField(default=True)
    content =  models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.titre

class Nouveaute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titre   =  models.CharField(max_length=200)
    image   =  models.ImageField(upload_to=image_path, null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titre


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Commenté {} par {}'.format(self.message, self.nom)