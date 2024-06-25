from django.urls import path
from django.urls import include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'rooms', views.ChatViewSet, basename='rooms')
router.register(r'messages', views.MessageViewSet, basename='messages')

urlpatterns = [
    path('', include(router.urls)),
]