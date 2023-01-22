from django.db import models


class Kelas(models.Model):
  nama = models.CharField(max_length=10)

  def __str__(self): 
    return self.nama

class Siswa(models.Model):
  nis = models.IntegerField(max_length=10)
  nama = models.CharField(max_length=50)
  kelas_id = models.ForeignKey(Kelas, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.nama

class Keterangan(models.Model):
  nama = models.CharField(max_length=50)

  def __str__(self):
    return self.nama

    
class Data(models.Model):
  tanggal = models.DateTimeField(auto_now=True)
  siswa_id = models.ForeignKey(Siswa, on_delete=models.CASCADE, null=True)
  keterangan_id = models.ForeignKey(Keterangan, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.nama
      

class Rincian(models.Model):
  id_data = models.ForeignKey(Data, on_delete=models.CASCADE)