# Generated by Django 4.1.1 on 2024-01-03 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='rating_goodreads',
            field=models.FloatField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')]),
        ),
        migrations.CreateModel(
            name='GambarBuku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar', models.ImageField(upload_to='covers/')),
                ('buku', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='gambar', to='buku.buku')),
            ],
        ),
    ]
