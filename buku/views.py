from typing import Any
from django.db.models.query import QuerySet
from .models import Buku

from django.views.generic import ListView, DetailView
# Create your views here.
class ListBukuView(ListView) :
    model = Buku
    template_name = "list_buku.html"
    context_object_name = 'daftar_buku'

class DetailBukuView(DetailView):
    model = Buku
    template_name = 'detail_buku.html'
    context_object_name = 'buku'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'
class RekomendasiBukuView(ListView):
    model = Buku
    template_name = "rekomendasi_buku.html"
    context_object_name = 'daftar_buku'
class RattingBukuView(ListView):
    model = Buku
    template_name = "ratting_buku.html"
    context_object_name = 'daftar_buku'
    queryset = Buku.objects.filter(rating_goodreads__gte=4).order_by('-rating_goodreads')
    
class SearchBukuView(ListView):
    template_name = 'list_buku.html'
    model = Buku
    context_object_name ="daftar_buku"
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Buku.objects.filter(judul__contains=query)
        print(object_list)
        return object_list