import os
import random
import uuid
import PIL.Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

from django.db import models

#dossier de stockage des images
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def image_path(instance, filename):
    new_filename = random.randint(1,3910209312)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "galerie/{new_filename}/{final_filename}".format(
            new_filename=new_filename,
            final_filename=final_filename)

class Image_long(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name  = models.CharField(max_length=200)
    statut = models.BooleanField(default=True)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)

    def save(self):
            #Opening the uploaded image
            im = PIL.Image.open(self.image)

            output = BytesIO()

            #Resize/modify the image
            im = im.resize( (472,708) )

            #after modifications, save it to the output
            im.save(output, format='JPEG', quality=100)
            output.seek(0)

            #change the imagefield value to be the newley modifed image value
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

            super(Image_long,self).save()

    def __str__(self):
        return self.name


class Image_large(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name  = models.CharField(max_length=200)
    statut = models.BooleanField(default=True)
    image = models.ImageField(upload_to=image_path, null=True, blank=True)

    def save(self):
            #Opening the uploaded image
            im = PIL.Image.open(self.image)

            output = BytesIO()

            #Resize/modify the image
            im = im.resize( (708,472) )

            #after modifications, save it to the output
            im.save(output, format='JPEG', quality=100)
            output.seek(0)

            #change the imagefield value to be the newley modifed image value
            self.image = InMemoryUploadedFile(output,'ImageField', "%s.jpg" %self.image.name.split('.')[0], 'image/jpeg', sys.getsizeof(output), None)

            super(Image_large,self).save()

    def __str__(self):
        return self.name