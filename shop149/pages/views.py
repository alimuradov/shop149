from rest_framework import viewsets

from django.shortcuts import render

from .models import Page
from .serializers import PageSerializer


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'


def index(request):
    return render(request, 'index.html')



