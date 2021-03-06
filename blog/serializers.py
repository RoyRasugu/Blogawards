from rest_framework import serializers
from blog.models import Profile, Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = [
            "ProjectId",
            "title", 
            "img_post", 
            "description",
            "project_url",
            "posted_by",
            "posted_on",   
        ]

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "ProfileId",
            "user",
            "profile_pic",
            "bio",
            "email",
            "updated_on",
        ]