from django.db import models


class Kelas(models.Model):
  nama = models.CharField(max_length=10)

  def __str__(self): 
    return self.nama

class Siswa(models.Model):
  nis = models.CharField(max_length=10)
  nama = models.CharField(max_length=50)
  kelas_id = models.ForeignKey(Kelas, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.nama

class Pelanggaran(models.Model):
  nama = models.CharField(max_length=50)

  def __str__(self):
    return self.nama

    
class Pelanggar(models.Model):
  tanggal = models.DateTimeField(auto_now=True)
  siswa = models.ForeignKey(Siswa, on_delete=models.CASCADE, null=True)
  pelanggaran = models.ForeignKey(Pelanggaran, on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.siswa.nama
      

