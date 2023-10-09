from django.db import models

# Create your models here.
class Projects(models.Model):
    project_title = models.CharField(max_length=200)
    technologies = models.CharField(max_length=200)
    project_image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=1000)

    def __str__(self):
        return self.project_title