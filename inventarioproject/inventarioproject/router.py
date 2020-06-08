from inventarioapi.viewsets import ProductoViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewset)