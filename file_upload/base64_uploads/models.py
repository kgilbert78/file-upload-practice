from django.db import models

# Create your models here.
class FileUpload(models.Model):
    doc = models.FileField(upload_to='docs/')

    def __str__(self) -> str:
        return self.doc