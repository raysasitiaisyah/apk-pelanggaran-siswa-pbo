from django.contrib import admin
from pelanggaransiswa.models import *

class DataAdmin(admin.ModelAdmin):
  list_display = ['tanggal', 'nama', 'kelas', 'keterangan',]

admin.site.register(Data, DataAdmin)