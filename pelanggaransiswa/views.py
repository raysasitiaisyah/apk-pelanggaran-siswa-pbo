from django.shortcuts import render, redirect
from django.contrib import messages
from pelanggaransiswa.forms import FormPelanggar
from django.conf import settings
from django.contrib.auth.decorators import login_required
from pelanggaransiswa.models import *

@login_required(login_url=settings.LOGIN_URL)
def hapus_siswa(request, id_pelanggar):
    pelanggar = Pelanggar.objects.filter(id=id_pelanggar)
    pelanggar.delete()
    
    messages.success(request, "Data berhasil dihapus!")
    return redirect('pelanggar')

@login_required(login_url=settings.LOGIN_URL)
def pelanggar(request):
    if request.POST:
        kata_kunci = request.POST['cari']
        pelanggars = Pelanggar.objects.filter(siswa__nama__contains=kata_kunci)
        konteks = {
            'pelanggars': pelanggars,
        }
    else:
        pelanggars = Pelanggar.objects.all()
        
        konteks = {
            'pelanggars' : pelanggars,
        }
    return render(request,'pelanggar.html', konteks)

@login_required(login_url=settings.LOGIN_URL)
def tambah_siswa(request):
    if request.POST:
        form = FormPelanggar(request.POST)
        if form.is_valid():
            form.save()
            form = FormPelanggar()
            pesan = "Data berhasil disimpan"
            
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return redirect('/pelanggar')
    else:
        form = FormPelanggar()

    konteks = {
        'form': form,
    }

    return render(request, 'tambah.html', konteks)
