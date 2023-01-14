from django.shortcuts import render


def data(request):
    nama = ["Raysa", "Rossa"]
    kelas = "12 RPL 1"

    konteks = {
        'name': nama,
        'kelas': kelas,
    }
    return render(request, 'data.html', konteks)
