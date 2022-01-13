from django.urls import path, include
from .routers import router

app_name = 'animals'

urlpatterns = [
    path('', include(router.urls)),
]
