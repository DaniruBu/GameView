from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import SimpleRouter
from blog.views import *

router = SimpleRouter()

router.register(r'topic', TopicViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('social_django.urls', namespace='social')),
    path('auth/', oauth),
] + router.urls