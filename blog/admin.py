from django.contrib import admin
from blog.models import Project, Profile, Review, Rating

# Register your models here.
admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Review)
admin.site.register(Rating)