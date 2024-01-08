from django.db import models
from django.utils.text import slugify
# Create your models here.
from django.db import models
from ckeditor.fields import RichTextField

class Buku(models.Model):
    id = models.AutoField(primary_key=True)
    judul = models.CharField(max_length=100)
    anak_judul = models.CharField(max_length=100, null = True, blank = True)
    sinopsis = RichTextField()
    pengarang = models.CharField(max_length=100)
    tahun = models.IntegerField()
    edisi = models.IntegerField()
    penerbit = models.CharField(max_length=100)
    tempat_terbit = models.CharField(max_length=100)
    topik = models.CharField(max_length=50)
    isbn = models.CharField(max_length=20)
    RATINGS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    
    rating_goodreads = models.FloatField(choices = RATINGS)
    rekomended = models.BooleanField(null=True, blank = True)
    slug = models.SlugField(default="", null=False)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.judul
    class Meta:
        verbose_name_plural = "Data Buku"

class GambarBuku(models.Model):
    buku = models.OneToOneField('Buku', on_delete=models.CASCADE, related_name='gambar')
    gambar = models.ImageField(upload_to='static/img/covers/')

    def __str__(self):
        return f"Gambar {self.buku.judul}"
    class Meta: 
        verbose_name_plural = "Gambar Buku"