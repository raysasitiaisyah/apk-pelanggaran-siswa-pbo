from django.contrib import admin
from pelanggaransiswa.models import *

class PelanggarAdmin(admin.ModelAdmin):
  list_display = ['tanggal', 'siswa', 'pelanggaran']


admin.site.register(Pelanggar, PelanggarAdmin)
admin.site.register(Kelas)
admin.site.register(Siswa)
admin.site.register(Pelanggaran)
