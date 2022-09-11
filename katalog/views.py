from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_catalog = CatalogItem.objects.all()
    context = {
        'list_barang' : data_barang_catalog,
        'nama' : 'Muhammad Rafialy Farrel',
        'id' : '2106751171',
    }
    return render(request, "katalog.html", context)