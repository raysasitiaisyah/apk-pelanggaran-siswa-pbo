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


def rincian_pelanggar(req, idpelanggar):
    pelanggar = Pelanggar.objects.get(id=idpelanggar)

    total = Pelanggar.objects.filter(id_pelanggar__id=idpelanggar).count()
    kesiangan = Pelanggar.objects.filter(id_pelanggar__id=idpelanggar).count()
    sepatu_putih = Pelanggar.objects.filter(id_pelanggar__id=idpelanggar).count()
    memakai_sendal = Pelanggar.objects.filter(id_pelanggar__id=idpelanggar).count()
    memakai_gelang = Pelanggar.objects.filter(id_pelanggar__id=idpelanggar).count()
    memakai_topi_bebas = Pelanggar.objects.filter(id_pelanggar__id=idpelanggar).count()


    template = 'rincian.html'
    konteks = {
        'pelanggars': pelanggar,
        'total': total,
        'kesiangan': kesiangan,
        'sepatu_putih': sepatu_putih,
        'memakai_sendal': memakai_sendal,
        'memakai_gelang': memakai_gelang,
        'memakai_topi_bebas': memakai_topi_bebas,

    }
    return render(req, template, konteks)