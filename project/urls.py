
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alloworign', views.AllowOriginViewSet)
router.register('iplist', views.IpListViewSet)
router.register('user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('apiview/',views.AllowOriginAPIView.as_view()),
    path('apiview/<int:id>/',views.AllowOriginAPIView.as_view()),
    path('apiview/<int:id>/update/',views.AllowOriginAPIView.as_view()),
    path('apiview/<int:id>/delete/',views.AllowOriginAPIView.as_view())
]
