from django.db import models
from django.utils.timezone import now
from django.utils import timezone
# Create your models here.


class File(models.Model):
    id_file  = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=50)
    file_data = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(
            default=timezone.now)
    updated_at =models.DateTimeField(
            default=timezone.now)
    deleted_at = models.DateTimeField(
            default=timezone.now)

    class Meta:
        verbose_name_plural = "Files"

    def __str__(self):
        return str(self.id_file)
    