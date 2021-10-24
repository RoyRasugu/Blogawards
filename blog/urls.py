from django.urls import path
from blog import views

urlpatterns = [
    path('api/profile/', views.ProfileList.as_view()),
    path('api/project/', views.ProjectList.as_view()),
]