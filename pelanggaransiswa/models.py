from django.db import models


class Data(models.Model):
    tanggal = models.DateTimeField(auto_now=True)
    nama = models.CharField(max_length=50)
    kelas = models.CharField(max_length=20)
    def __str__(self):
      return self.nama
      
class Pelanggar(models.Model):
    pilih_ket = (
      ('K', 'KESIANGAN')
    )
    keterangan = models.CharField(max_length=50, choices=pilih_ket)