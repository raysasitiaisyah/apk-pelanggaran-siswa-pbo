from django.contrib import admin
from django.urls import path
from pelanggaransiswa.views import data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', data),
]