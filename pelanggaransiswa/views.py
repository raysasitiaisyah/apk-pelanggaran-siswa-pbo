from django.shortcuts import render
from pelanggaransiswa.forms import FormData
from pelanggaransiswa.models import *

def data(request):
    datas = Data.objects.all()
    
    konteks = {
        'datas' : datas,
    }
    return render(request,'data.html', konteks)

def tambah_siswa(request):
    if request.POST:
        form = FormData(request.POST)
        if form.is_valid():
            form.save()
            form = FormData()
            pesan = "Data berhasil disimpan"
            
            konteks = {
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'tambah-siswa.html', konteks)
    else:
        form = FormData()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah-siswa.html', konteks)