from django.shortcuts import render, redirect
from django.contrib import messages
from pelanggaransiswa.forms import FormData
from django.conf import settings
from pelanggaransiswa.models import *


def hapus_siswa(request, id_buku):
    data = Data.objects.filter(id=id_buku)
    data.delete()
    
    messages.success(request, "Data berhasil dihapus!")
    return redirect('buku')


def data(request):
    if request.POST:
        kata_kunci = request.POST['cari']
        datas = Data.objects.filter(nama__contains=kata_kunci)
        konteks = {
            'datas': datas,
        }
    else:
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
                'form': form,
                'pesan': pesan,
            }
            return render(request,'tambah.html', konteks)
    else:
        form = FormData()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah.html', konteks)