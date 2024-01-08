from django.urls import path
from .views import *
urlpatterns = [
    path("", ListBukuView.as_view(), name="daftar-buku"),
    path("rekomendasi", RekomendasiBukuView.as_view(), name="rekomendasi-buku"),
    path("ratting", RattingBukuView.as_view(), name="ratting-buku"),
    path("search", SearchBukuView.as_view(),name="search-buku"),
    path('buku/<slug:slug>/', DetailBukuView.as_view(), name='detail-buku'),
]
