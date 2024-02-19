from django.db import models

# Create your models here.

class Keyword(models.Model):
    associated_keyword = models.CharField(
        max_length=200
    )  # may change length - coordinate it with keyword output params

    def __str__(self) -> str:
        return self.associated_keyword
    
class FileWithKeywords(models.Model):
    keyword_doc = models.FileField(upload_to='keyword_docs/')
    keyword = models.ManyToManyField(Keyword)

    def __str__(self) -> str:
        return self.keyword_doc