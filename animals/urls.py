from django.urls import path, include
from .routers import family_router

app_name = 'animals'

urlpatterns = [
    path('', include(family_router.urls)),
]


