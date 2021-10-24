from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    img_post = models.ImageField(upload_to="project/")
    description = HTMLField()
    project_url = models.URLField()
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    posted_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="profile/")
    bio = HTMLField()
    email = models.EmailField()
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

class Review(models.Model):
    review = HTMLField()
    posted_on = models.DateTimeField(auto_now_add=True) 
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, null=True) 


class Rating(models.Model):
    content = models.IntegerField(default=1)
    design = models.IntegerField(default=1)
    usability = models.IntegerField(default=1)
    vote_on = models.DateTimeField(default=1)
    vote_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    