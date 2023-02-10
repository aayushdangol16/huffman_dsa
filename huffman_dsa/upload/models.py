from django.db import models

class FilesUpload(models.Model):
    file=models.FileField()