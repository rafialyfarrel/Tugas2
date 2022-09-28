# Tugas 4 PBP README.md
### Muhammad Rafialy Farrel
### 2106751171
### PBP-A

#

### [Link Aplikasi Heroku](https://bismillahgol.herokuapp.com/todolist/login/)

## 1. Apa kegunaan ```{% csrf_token %}``` pada elemen ```<form>?``` Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen ```<form>```?
Kegunaan dari ```{% csrf_token %}``` pada elemen ```<form>?``` yaitu sebuah string yang di-generate untuk mengcompare nilai unik dari csrf_token di saat user ingin mengakses 
method POST dan elemen ```form``` akan menyetujui jika user mengaksesnya dengan benar dan akan selalu diperbarui saat user mereload data sehingga tidak dapat disalahgunakan.
Jika tidak terdapat potongan kode ```{% csrf_token %}``` pada elemen ```form``` akan menyebabkan munculnya link yang dapat diakses oleh orang lain dan terjadi suatu hal yang 
tidak diinginkan.

## 2. Apakah kita dapat membuat elemen ```<form>``` secara manual (tanpa menggunakan generator seperti ```{{ form.as_table }})```? Jelaskan secara gambaran besar bagaimana cara 
      membuat ```<form>``` secara manual.
Iya kita dapat membuat elemen ``<form>``` secara manual. Hal yang perlu dilakukan yaitu ```{% csrf_token %}```, membuat method POST, dan membuat form dengan tabel yang dibuat 
pada html, dan menggunakan form pada context untuk mengupdate form.

## 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada 
      template HTML.
Pertama user mengisi data melalui HTML form dan mensubmit data dengan menekan tombol submit. Lalu, data tersebut disimpan di database django yang nantinya dapat diakses sesuai
dengan user menggunakan ```todolistItem.objects.filter(user=user)``` dan di masukkan ke dalam context dan di return ke html. Lalu, menjalankan loop yang berisikan data pada 
```item.list_data``` dan ditampilkan kepada user.

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

a). Menjalankan command ```python manage.py startapp todolist``` pada folder ```PBP_Tugas\Tugas2```
b). Menambahkan aplikasi todolist pada ```prodject_django\settings.py```
c). Menambahkan ```path('todolist/', include('todolist.urls')),``` pada ``````prodject_django\urls.py```
d). Membuat ```todolist\models.py``` yang berisikan object dengan fields sesuai dengan yang ditugaskan
e). Membuat form registrasi, login, dan logout dengan menghubungkannya ke register.html, login.html, todolist.html dengan syarat harus login terlebih dahulu menggunakan
    ```@login_required(login_url='/todolist/login/')```
f). Membuat halaman utama yang berisi object yang sesuai pada ```todolist\models.py```, tombol ```Create Task``` membuka halaman baru untuk user menambahkan title dan 
    description yang ketika disubmit oleh user akan disimpan ke dalam database django, dan tombol ```Logout``` membuka halaman utama seperti saat sebelum login. Ketiga hal ini
    sudah diatur pada ```todolist\views.py```
g). Membuat dua akun pengguna dan tiga dummy data menggunakan model ```Task``` pada akun masing-masing di situs web Heroku.

## Referensi
   1. https://docs.djangoproject.com/en/4.1/ref/models/fields/#foreignkey
   2. https://docs.djangoproject.com/en/4.1/ref/contrib/auth/
   3. https://docs.djangoproject.com/en/4.1/topics/forms/
