from django.db import models


class File(models.Model):
    title = models.CharField(max_length=256)
    purpose = models.CharField(max_length=256, blank=True)
    files = models.FileField(upload_to="files", max_length=100)

    def __str__(self):
        return self.title
