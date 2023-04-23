from django.contrib import admin
from django.urls import path, include
from book.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('book.urls')),
]
