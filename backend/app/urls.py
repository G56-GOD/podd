from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthVS, FathMVS, KidMVS


router = DefaultRouter()
router.register(r'auth', AuthVS, basename='auth')
router.register(r'faths', FathMVS, basename='faths')
router.register(r'kids', KidMVS, basename='kids')

urlpatterns = [
    path('', include(router.urls))
]