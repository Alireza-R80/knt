from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(designer=self.request.user)


# Create your views here.
