from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Use your actual app name
]

# Custom 404 handler (optional, see views.py below)
handler404 = 'main.views.custom_404'

