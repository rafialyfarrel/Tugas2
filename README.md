# Tugas 2 PBP README.md
### Muhammad Rafialy Farrel
### 2106751171
### PBP-A

#

### [Link Aplikasi Heroku](https://bismillahgol.herokuapp.com/katalog/)

#

## Penjelasan Alur

Tahap pertama dari alur program Tugas 2 ini adalah user/client memberikan request yang diproses oleh ```urls.py``` untuk mendefinisikan alamat URL. Pada tahap kedua ```urls.py``` melanjutkannya ke fungsi ```views.py``` yang sudah sesuai dengan url. Pada tahap ketiga ```views.py``` mengambil data dari ```models.py``` yang akan ditampilkan dan disesuaikan dengan ```katalog.html```. Setelah data sudah terisi ke dalam ```katalog.html``` akan diteruskan ke user/client berupa HTTP.

## Jelaskan kenapa menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?
Dalam hal ini, penggunaan virtual environment dalam project berbasis python sangat direkomendasikan, tetapi bukan berarti wajib untuk menggunakannya. 
Virtual environment merupakan suatu tools untuk menjaga ruang yang terpisah dalam sebuah proyek dan terisolasi dari dependensi utama. 
Karena hal ini, virtual environment berguna ketika kita memerlukan dependensi yang berbeda saat membuat proyek pada satu sistem operasi yang sama. 
Kebutuhan atau dependensi yang berbeda-beda ini akan menimbulkan crash pada proyek. Oleh karena itu, penting bagi kita untuk menggunakan virtual environment 
karena dapat menjalankan suatu proyek tanpa merubah konfigurasi pada sistem operasi yang kita miliki.

## Jelaskan bagaimana cara kamu mengimplementasikan poin 1 sampai dengan 4 di atas.

### ```urls.py```
```
from django.urls import path
from katalog.views import show_katalog

app_name = 'katalog'

urlpatterns = [
    path('', show_katalog, name = 'show_katalog'),
]
```

## ```views.py```
```
def show_katalog(request):
    data_barang_catalog = CatalogItem.objects.all()
    context = {
        'list_barang' : data_barang_catalog,
        'nama' : 'Muhammad Rafialy Farrel',
        'id' : '2106751171',
    }
    return render(request, "katalog.html", context)
```

## ```katalog.html```
```
...
{% for item in list_barang %}
    <tr>
        <th>{{item.item_name}}</th>
        <th>{{item.item_price}}</th>
        <th>{{item.item_stock}}</th>
        <th>{{item.rating}}</th>
        <th>{{item.description}}</th>
        <th>{{item.item_url}}</th>
    </tr>
...
```
