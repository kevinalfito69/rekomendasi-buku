# Generated by Django 4.1.1 on 2024-01-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0003_buku_sinopsis_alter_gambarbuku_gambar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='anak_judul',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
