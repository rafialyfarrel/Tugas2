# Tugas 6 PBP README.md
### Muhammad Rafialy Farrel
### 2106751171
### PBP-A

## 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming
Cara kerja syncronus adalah user harus menunggu server memberikan respon kepada user di saat user memberikan request atau menekan suatu opsi di dalam web tersebut dan dia akan merefresh secara keseluruhan. 
Sedangkan asyncronus adalah server tidak akan merefresh secara keseluruhan dan user dapat tetap beriteraksi dengan tampilan yang sedang dilihat atau yang sedang dipilih (modul tidak perlu menunggu task lain selesai berjalan).

## 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini
Maksud dari penerapan paradigma Event-Driven Programming ini yaitu digunakan untuk meng-handle event atau memberikan feedback kepada user setelah menekan sebuah tombol. 
Terdapat sebuah function javaScript yang dibuat dan dipetakan sebagai sebuah fungsi yang akan dijalankan ketika event dilakukan oleh user. 
Pada todolist.html saya terapkan pada ```createtask```. Di saat user menekan tombol createtask, user akan mengisi form berisi task yang nantinya akan ditampilkan kembali sesuai dengan yang sudah diisi oleh user.

## 3.  Jelaskan penerapan asynchronous programming pada AJAX
 AJAX merupakan sebuah konsep yang menerapkan asynchronous programming dalam mengeksekusi task pada program. Pertama-tama browser akan memanggil AJAX javascript untuk mengaktifkan XMLHttpRequest dan mengirimkan HTTP Request ke server,
 XMLHttpRequest dibuat untuk proses pertukaran data di server secara asinkron, server menerima, memproses, dan mengirimkan data kembali ke browser, lalu browser menerima data dari user dan langsung ditampilkan di halaman website, tanpa 
 perlu reload atau membuat halaman baru.
 
## 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas
1. Saya menambahkan sebuah def views baru untuk mengambil data dari models.py dan direpresentasikan sebagai JSON serta meng-importnya ke dalam ```urls.py```
2. Saya membuat beberapa fungsi get data menggunakan ajax pada todolist.html
3. Membuat modal dengan template pada Bootstrap di todolist.html. Lalu saya mengubah link pemetaan setelah meng-click tombol CreateTask menuju target modal.
4. Membuat views baru untuk menambahkan data dan memetakannya kedalam URL sebelum membuat fungsi AJAX
5. Lalu saya membuat fungsi AJAX pada todolist.html dengan type POST untuk menambahkan data dari user
6. Fitur ```createtask``` akan di reload secara asynchronous
