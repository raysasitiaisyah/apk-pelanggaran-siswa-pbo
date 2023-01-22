from django.forms import ModelForm
from django import forms
from pelanggaransiswa.models import Data

class FormData(ModelForm):
  class Meta:
    model = Data
    fields = '__all__'

    widgets = {
      'tanggal' : forms.DateTimeInput({'class' : 'form-control'}),
      'nama' : forms.Select({'class' : 'form-control'}),
      'keterangan' : forms.Select({'class' : 'form-control'}),
    }

