# Generated by Django 3.2.16 on 2023-01-23 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pelanggaransiswa', '0010_auto_20230122_0845'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Keterangan',
            new_name='Pelanggaran',
        ),
        migrations.RenameField(
            model_name='data',
            old_name='keterangan_id',
            new_name='pelanggaran_id',
        ),
    ]
