from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    img_post = models.ImageField(upload_to="project/")
    description = HTMLField()
    project_url = models.URLField()
    posted_on = models.DateTimeField(auto_now_add=True)
    