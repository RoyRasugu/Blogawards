from django.urls import path
from blog.views import projectApi
from django.conf import settings
from django.conf.urls.static import static

from award_clone.settings import MEDIA_ROOT

urlpatterns = [
    path('project/', projectApi),
    path('project/([0-9]+)', projectApi),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = MEDIA_ROOT)