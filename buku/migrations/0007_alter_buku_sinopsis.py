# Generated by Django 4.1.1 on 2024-01-06 04:42

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buku', '0006_buku_rekomended'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='sinopsis',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
