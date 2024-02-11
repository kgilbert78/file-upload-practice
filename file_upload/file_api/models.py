from django.db import models

# Create your models here.
class File(models.Model):
    document = models.FileField(upload_to='documents/')

    def __str__(self) -> str:
        return self.document