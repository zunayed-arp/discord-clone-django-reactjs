
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('frontend.urls')),
    path('api/',include('authy.api_urls')),
]
