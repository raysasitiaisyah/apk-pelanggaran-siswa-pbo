from django.contrib import admin
from django.urls import path
from pelanggaransiswa.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data/', data, name='data'),
    path('tambah/', tambah_siswa, name='tambah_siswa'),
    path('data/hapus/<int:id_data>', hapus_siswa, name='hapus_siswa'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('data/<int:iddata>/', rincian_pelanggar),
]