from rest_framework import viewsets
from . import models
from . import serializers

class ProductoViewset(viewsets.ModelViewSet):
    queryset = models.Producto.objects.all()
    serializer_class = serializers.ProductoSerializer
    