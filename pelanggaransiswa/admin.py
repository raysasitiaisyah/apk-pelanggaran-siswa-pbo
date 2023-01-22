from django.contrib import admin
from pelanggaransiswa.models import *

class DataAdmin(admin.ModelAdmin):
  list_display = ['tanggal', 'siswa_id', 'keterangan_id']

class PelanggarAdmin(admin.ModelAdmin):
  list_display = ['id_data']


admin.site.register(Data, DataAdmin)
admin.site.register(Kelas)
admin.site.register(Siswa)
admin.site.register(Keterangan)
admin.site.register(Rincian, PelanggarAdmin)
