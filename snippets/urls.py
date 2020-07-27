from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views
from django.contrib import admin

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)