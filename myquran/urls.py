from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    # Examples:
    path('', include('myapp.urls')),    
    path('admin/', admin.site.urls),
]
