from django.shortcuts import render, redirect
from django.contrib import messages
from pelanggaransiswa.forms import FormData
from django.conf import settings
from django.contrib.auth.decorators import login_required
from pelanggaransiswa.models import *

@login_required(login_url=settings.LOGIN_URL)
def hapus_siswa(request, id_data):
    data = Data.objects.filter(id=id_data)
    data.delete()
    
    messages.success(request, "Data berhasil dihapus!")
    return redirect('data')

@login_required(login_url=settings.LOGIN_URL)
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

@login_required(login_url=settings.LOGIN_URL)
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

