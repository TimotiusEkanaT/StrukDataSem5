import unittest
from ug5 import Buku

class TestBuku(unittest.TestCase):

    def setUp(self):
        self.buku_fiksi = Buku("Novel Klasik", "Penulis A", 1970, "Fiksi", 100000)
        self.buku_nonfiksi = Buku("Ilmu Pengetahuan", "Penulis B", 2000, "Nonfiksi", 150000)

    def test_judul(self):
        self.assertEqual(self.buku_fiksi.judul, "Novel Klasik")
        self.assertEqual(self.buku_nonfiksi.judul, "Ilmu Pengetahuan")

    def test_penulis(self):
        self.assertEqual(self.buku_fiksi.penulis, "Penulis A")
        self.assertEqual(self.buku_nonfiksi.penulis, "Penulis B")


    def test_tahunTerbit(self):
        self.assertEqual(self.buku_fiksi.tahunTerbit,1970)
        self.assertEqual(self.buku_nonfiksi.tahunTerbit,2000)


    def test_jenis(self):
        self.assertEqual(self.buku_fiksi.jenis, "Fiksi")
        self.assertEqual(self.buku_nonfiksi.jenis, "Nonfiksi")

    def test_harga(self):
        self.assertEqual(self.buku_fiksi.harga, 100000)
        self.assertEqual(self.buku_nonfiksi.harga, 150000)

    # def test_set_judul(self):
    #     self.buku_fiksi.judul = "Belajar Python Lanjutan"
    #     self.assertEqual(self.buku_fiksi.judul, "Belajar Python Lanjutan")

    # def test_set_penulis(self):
    #     self.buku_fiksi.penulis = "Jane Doe"
    #     self.assertEqual(self.buku_fiksi.penulis, "Jane Doe")

    # def test_set_tahunTerbit(self):
    #     """Uji getter dan setter untuk tahun terbit."""
    #     self.buku_fiksi.tahunTerbit = 2021
    #     self.assertEqual(self.buku_fiksi.tahunTerbit, 2021)

    # def test_set_jenis(self):
    #     """Uji getter dan setter untuk jenis."""
    #     self.buku_fiksi.jenis = "Teknologi"
    #     self.assertEqual(self.buku_fiksi.jenis, "Teknologi")

    # def test_set_harga(self):
    #     """Uji getter dan setter untuk harga."""
    #     self.buku_fiksi.harga = 200000
    #     self.assertEqual(self.buku_fiksi.harga, 200000)

    def test_umurBuku(self):
        self.assertEqual(self.buku_fiksi.umurBuku(), 54)
        self.assertEqual(self.buku_nonfiksi.umurBuku(), 24)


    def test_hargaBuku(self):
        self.assertEqual(self.buku_fiksi.hargaBuku(), 90000.0)
        self.assertEqual(self.buku_nonfiksi.hargaBuku(), 147000.0)



if __name__ == '__main__':
    unittest.main()
