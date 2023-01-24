from django.contrib import admin
from django.urls import path
from pelanggaransiswa.views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pelanggar/', pelanggar, name='pelanggar'),
    path('tambah/', tambah_siswa, name='tambah_siswa'),
    path('pelanggar/hapus/<int:id_pelanggar>', hapus_siswa, name='hapus_siswa'),
    path('', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('pelanggar/<int:pelanggar_id>/', rincian_pelanggar),
]