from django.shortcuts import render
from rest_framework import viewsets

from .permissions import GetOnly
from .serializers import *


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (GetOnly,)

    def perform_create(self, serializer):
        serializer.save(designer=self.request.user)

# Create your views here.
