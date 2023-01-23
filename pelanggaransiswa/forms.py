from django.forms import ModelForm
from django import forms
from pelanggaransiswa.models import Pelanggar

class FormPelanggar(ModelForm):
  class Meta:
    model = Pelanggar
    fields = '__all__'

    widgets = {
      'tanggal' : forms.DateTimeInput({'class' : 'form-control'}),
      'siswa' : forms.Select({'class' : 'form-control', 'data-live-search':"true"}),
      'pelanggaran' : forms.Select({'class' : 'form-control'}),
    }
