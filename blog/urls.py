from django.urls import path
from blog.views import home, register, login, ProfileList, ProjectList
from django.conf import settings
from django.conf.urls.static import static

from award_clone.settings import MEDIA_ROOT

urlpatterns = [
    path('', home, name='home'),
    path('signup', register, name='register'),
    path('login', login, name='login'),
    path('api/profile/', ProfileList.as_view()),
    path('api/project/', ProjectList.as_view()),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = MEDIA_ROOT)