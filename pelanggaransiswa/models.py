from django.db import models


class Data(models.Model):
    pilih_ket = {
      ('kesiangan', 'k'),
      ('ses', 's'),
    }
    tanggal = models.DateTimeField(auto_now=True)
    nama = models.CharField(max_length=50)
    kelas = models.CharField(max_length=20)
    keterangan = models.CharField(max_length=50, choices=pilih_ket)
    jumlah_poin = models.IntegerField(null=True)

def __str__(self):
  return self.nama

