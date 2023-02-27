from django.urls import include, path
from .views import RoomView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'music', RoomView)



urlpatterns = [
    path('', include(router.urls)),
]
