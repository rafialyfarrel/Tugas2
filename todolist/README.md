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

## 2. Apakah kita dapat membuat elemen ```<form>``` secara manual (tanpa menggunakan generator seperti ```{{ form.as_table }})```? Jelaskan secara gambaran besar bagaimana cara membuat ```<form>``` secara manual.
Iya kita dapat membuat elemen ```<form>``` secara manual. Hal yang perlu dilakukan yaitu ```{% csrf_token %}```, membuat method POST, dan membuat form dengan tabel yang dibuat 
pada html, dan menggunakan form pada context untuk mengupdate form.

## 3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada           template HTML.
Pertama user mengisi data melalui HTML form dan mensubmit data dengan menekan tombol submit. Lalu, data tersebut disimpan di database django yang nantinya dapat diakses sesuai
dengan user menggunakan ```todolistItem.objects.filter(user=user)``` dan di masukkan ke dalam context dan di return ke html. Lalu, menjalankan loop yang berisikan data pada 
```item.list_data``` dan ditampilkan kepada user.

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

#### a). Menjalankan command ```python manage.py startapp todolist``` pada folder ```PBP_Tugas\Tugas2```

#### b). Menambahkan aplikasi todolist pada ```prodject_django\settings.py```

#### c). Menambahkan ```path('todolist/', include('todolist.urls')),``` pada ```prodject_django\urls.py```

#### d). Membuat ```todolist\models.py``` yang berisikan object dengan fields sesuai dengan yang ditugaskan

#### e). Membuat form registrasi, login, dan logout dengan menghubungkannya ke register.html, login.html, todolist.html dengan syarat harus login terlebih dahulu menggunakan
    ```@login_required(login_url='/todolist/login/')```

#### f). Membuat halaman utama yang berisi object yang sesuai pada ```todolist\models.py```, tombol ```Create Task``` membuka halaman baru untuk user menambahkan title dan 
    description yang ketika disubmit oleh user akan disimpan ke dalam database django, dan tombol ```Logout``` membuka halaman utama seperti saat sebelum login. Ketiga hal ini
    sudah diatur pada ```todolist\views.py```

#### g). Membuat dua akun pengguna dan tiga dummy data menggunakan model ```Task``` pada akun masing-masing di situs web Heroku.

## Referensi
   1. https://docs.djangoproject.com/en/4.1/ref/models/fields/#foreignkey
   2. https://docs.djangoproject.com/en/4.1/ref/contrib/auth/
   3. https://docs.djangoproject.com/en/4.1/topics/forms/

#

# Tugas 5 PBP README.md
### Muhammad Rafialy Farrel
### 2106751171
### PBP-A

#

## 1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
a). Internal CSS merupakan kode CSS yang berada di dalam tag <style> dan kode HTML dituliskan di bagian atas (header) file HTML. Internal CSS dapat digunakan untuk membuat tampilan yang unik pada satu halaman website dan tidak digunakan pada halaman website yang lain.

Kelebihan Internal CSS:
1. Perubahan pada Internal CSS hanya berlaku pada satu halaman saja.
2. Anda tidak perlu melakukan upload beberapa file karena HTML dan CSS berada dalam satu file.
3. Class dan ID bisa digunakan oleh internal stylesheet.
    
Kekurangan Internal CSS:
1. Tidak efisien apabila Anda ingin menggunakan CSS yang sama dalam beberapa file.
2. Web menjadi lebih lamban saat di-reload jika CSS yang dibuat berbeda-beda setiap halaman.

b). Eksternal CSS merupakan kode CSS yang ditulis terpisah dengan kode HTML Eksternal CSS ditulis di sebuah file khusus yang berekstensi .css. File eksternal CSS biasanya diletakkan setelah bagian <head> pada halaman. Cara ini lebih sederhana dan simpel daripada menambahkan kode CSS di setiap elemen HTML yang ingin Anda atur tampilannya. 

Kelebihan Eksternal CSS:
1. Ukuran file HTML akan menjadi lebih kecil dan struktur dari kode HTML jadi lebih rapih.
2. Loading website menjadi lebih cepat.
3. File CSS dapat digunakan di beberapa halaman website sekaligus.
    
Kekurangan Internal CSS:
1. Halaman akan menjadi berantakan, ketika file CSS gagal dipanggil oleh file HTML. Hal ini terjadi disebabkan karena koneksi internet yang lambat.

c). Inline CSS merupakan kode CSS yang ditulis langsung pada atribut elemen HTML. Setiap elemen HTML memiliki atribut style untuk menulis inline CSS.

Kelebihan Inline CSS:
1. Sangat membantu ketika kita hanya ingin menguji dan melihat perubahan pada satu elemen.
2. Berguna untuk memperbaiki kode dengan cepat.
3. Proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat.

Kekurangan Internal CSS:
1. Tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.

## 2. Jelaskan tag HTML5 yang kamu ketahui.
1. <h1> to <h6>     = Tag untuk membuat heading sesuai dengan ukuran darii terbesar ke terkecil
2. <head>           = Tag untuk mendefisikan kepala dari sebuah halaman
3. <body>           = Tag untuk membuat tubuh dari sebuah halaman
4. <!DOCTYPE> 	    = Tag untuk menentukan tipe dokumen
5. <p> 	            = Tag untuk membuat paragraf
6. <br> 	        = Memasukan satu baris putus
7. <form> 	        = Tag untuk membuat sebuah form HTML untuk input pengguna
8. <button> 	    = Tag untuk membuat sebuah tombol yang dapat diklik
9. <nav> 	        = Tag untuk membuat navigasi link
10. <div> 	        = Tag untuk membuat sebuah bagian dalam dokumen
11. dan lain-lain masih banyak lagi
    
## 3. Jelaskan tipe-tipe CSS selector yang kamu ketahui.
1. .X                 = untuk merubah beberapa objek pada html dengan settingan yang sama
2. #X                 = semua elemen dalam X
3. "*"                = semua elemen pada halaman
4. element(p,h5,dll)  = semua elemen dengan tag html tersebut
5. :hover             = style css pada elemen akan berubah ketika pointer berada di atas elemen HTML
6. .<nama class>      = akan menerapkan styling untuk setiap elemen yang memiliki class sesuai nama
7. dan lain-lain masih banyak lagi

## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
1. Membuat tampilan website sebagus dan semenarik mungkin
   Mencari template di internet dan mengubahnya sesuai dengan tugas yang disuruh
2. Menggunakan cards untuk menampilkan isi dari task yang dibuat oleh user
3. Membuat tampilan website menjadi responsif
    
## Referensi
   1. https://www.niagahoster.co.id/blog/perbedaan-internal-external-dan-inline-css/
   2. https://gilacoding.com/read/tag-tag-pada-html-beserta-fungsinya
   3. https://code.tutsplus.com/id/tutorials/the-30-css-selectors-you-must-memorize--net-16048
