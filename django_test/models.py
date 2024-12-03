from django.db import models
from datetime import datetime
import os

def student_image_upload_path(instance, filename):
    name = instance.name.replace(' ', '_')
    surname = instance.surname.replace(' ', '_')
    extension = filename.split('.')[-1]
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    new_filename = f"{name}_{surname}_{timestamp}.{extension}"
    return os.path.join('collected-faces', new_filename)

class Student(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    image = models.ImageField(upload_to=student_image_upload_path, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
