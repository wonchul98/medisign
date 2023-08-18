from rest_framework.routers import DefaultRouter
from .views import WidgetViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'widget_list', WidgetViewSet)

app_name = 'widgets'
urlpatterns = [
    # ... your other URL patterns ...
    path('', include(router.urls)),
]