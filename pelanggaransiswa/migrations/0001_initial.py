# Generated by Django 3.2.16 on 2023-01-12 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('nama', models.CharField(max_length=50)),
                ('kelas', models.CharField(max_length=20)),
                ('jurusan', models.CharField(max_length=50)),
                ('keterangan', models.CharField(max_length=50)),
                ('jumlah_poin', models.IntegerField(max_length=10)),
            ],
        ),
    ]
