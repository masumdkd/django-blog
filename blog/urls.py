from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    path('authors/', include('django.contrib.auth.urls')),
    path('authors/', include('authors.urls')),
]
