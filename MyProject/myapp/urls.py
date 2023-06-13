from django.urls import path, include
from rest_framework import routers
from myapp.views import UserViewSet, ClientViewSet, ProjectViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
