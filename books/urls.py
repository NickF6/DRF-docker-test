from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('customer', views.CustomerModelViewSet, basename='customer')
router.register('book', views.BookModelViewSet, basename='book')
urlpatterns = router.urls
