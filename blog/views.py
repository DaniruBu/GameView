from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from blog.serializers import TopicSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from blog.models import Topic


class TopicViewSet(ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    filter_fields = ['title']
    search_fields = ['user']
    ordering_fields = ['title, user']

def oauth(request):
    return render(request, 'oauth.html')
