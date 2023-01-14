from django.db import models

# Create your models here.
class Data(models.Model):
    tanggal = models.DateField(auto_now=True)
    nama = models.CharField(max_length=50)
    kelas = models.CharField(max_length=20)
    jurusan = models.CharField(max_length=50)
    keterangan = models.CharField(max_length=50)
    jumlah_poin = models.IntegerField(null=True )

def __str__(self):
  return self.nama