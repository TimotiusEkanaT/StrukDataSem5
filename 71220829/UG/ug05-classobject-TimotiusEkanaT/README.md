[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/qJb96Lem)
# UG05_ClassObject

Buatlah suatu Class bernama Buku yang memiliki atribut judul, penulis, tahun rilis, jenis, dan harga asli buku (harga buku sebelum diskon). Class harus memiliki constructor yang menginisialisasikan nilai  judul, penulis, tahun rilis, jenis, dan harga asli buku.

Buatlah fungsi umurBuku, hargaBuku dan printInformasi

Fungsi printInformasi berisi judul, penulis, dan tahun terbit  dari Class Buku. 

Fungsi umurBuku digunakan untuk menghitung umur buku sejak terbit hingga tahun ini (2023).

Fungsi hargaBuku digunakan untuk menghitung harga buku setelah diskon. Jika buku berjenis “fiksi” maka akan diberi diskon 5%, jika berjenis “nonfiksi” maka akan diberi diskon 2%, dan jika umur buku lebih dari 50 tahun maka akan diberi diskon 10% berlaku untuk seluruh buku (fiksi dan nonfiksi juga termasuk).

Read me if you need


Class : Buku


Atribut :

• judul		: menyimpan data string judul buku

• penulis	: menyimpan data string penulis buku

• tahunTerbit	: menyimpan data integer tahun terbit buku

• jenis 		: menyimpan data string jenis buku

• harga		: menyimpan data integer atau float harga buku


Fungsi/Method :

• constructor : menginisialisasikan nilai atribut judul, penulis, tahun rilis, jenis, dan harga

• getter setter semua atribut : mengambil nilai baru ke atribut

• printInformasi : mencetak data atribut yang dimiliki object

• umurBuku : menghitung umur buku dari tahun ini - tahun terbit

• hargaBuku : menghitung harga buku setelah diskon





TEST CASE

if __name__ == "__main__":
    buku = Buku("Logika Matematika", "J Karel Tampubolon", 2000, "fiksi", 50000)
    buku.printInformasi()
    buku.hargaBuku()
    print(f"Umur buku: {buku.umurBuku()} tahun")


