
from django.contrib import admin
from django.urls import path,include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('ip/',include('aoip.urls')),
    path('',include('project.urls')),
    # path('student/',include('students.urls', namespace='student')),
    #  path('__debug__/', include('debug_toolbar.urls')),
]
