# Generated by Django 3.2.16 on 2023-01-22 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pelanggaransiswa', '0005_auto_20230119_1034'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keterangan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='data',
            name='keterangan',
        ),
        migrations.AddField(
            model_name='data',
            name='keterangan_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pelanggaransiswa.keterangan'),
        ),
    ]