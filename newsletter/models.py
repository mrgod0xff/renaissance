from django.db import models
import uuid
# Create your models here.

class Newsletter(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom   = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email
