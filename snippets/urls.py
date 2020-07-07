from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets import views
from django.contrib import admin

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# urlpatterns = format_suffix_patterns([
#     path('admin/', admin.site.urls),
#     path('snippets/',
#          views.SnippetList.as_view(),
#          name='snippet-list'),
#     path('snippets/<int:pk>/',
#          views.SnippetDetail.as_view(),
#          name='snippet-detail'),
#     path('snippets/<int:pk>/highlight/',
#          views.SnippetHighlight.as_view(),
#          name='snippet-highlight'),
#     path('users/',
#          views.UserList.as_view(),
#          name='user-list'),
#     path('users/<int:pk>/',
#          views.UserDetail.as_view(),
#          name='user-detail')
# ])
