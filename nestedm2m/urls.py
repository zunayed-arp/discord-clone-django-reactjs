
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('recipie',views.RecipieView)



urlpatterns = [
    path('allow-origin/',views.AllowOriginAPIView.as_view())
]+router.urls