"""
URL configuration for worldqna project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from home.views import custom_404, custom_500_view  # Make sure to import the custom_500_view
from django.conf.urls import handler404, handler500  # Import handler500 as well

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Include home.urls for specific paths related to your home app
    path('<path:not_found>/', custom_404),  # Catch-all for 404 errors
]

if not settings.DEBUG:
    handler404 = 'home.views.custom_404'  # Set custom_404 as the 404 handler
    handler500 = 'home.views.custom_500_view'  # Set custom_500_view as the 500 handler
