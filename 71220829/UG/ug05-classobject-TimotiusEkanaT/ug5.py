class Buku:

    def __init__(self, judul, penulis, tahunRilis, jenis, hargaAsliBuku):
        self._judul = judul
        self._penulis = penulis
        self._tahunRilis = tahunRilis
        self._jenis = jenis
        self._hargaAsliBuku = hargaAsliBuku

    #buat getter setter
    @property
    def judul(self):
        return self._judul

    @judul.setter
    def judul(self, value):
        self._judul = value

    @property
    def penulis(self):
        return self._penulis

    @penulis.setter
    def penulis(self, value):
        self._penulis = value

    @property
    def tahunTerbit(self):
        return self._tahunRilis

    @tahunTerbit.setter
    def tahunTerbit(self, value):
        self._tahunRilis = value

    @property
    def jenis(self):
        return self._jenis

    @jenis.setter
    def jenis(self, value):
        self.jenis = value


    @property
    def harga(self):
        return self._hargaAsliBuku

    @harga.setter
    def harga(self, value):
        self._hargaAsliBuku = value


    def printInformasi(self):
        print("Judul: ", self.judul, "\nPenulis: ", self.penulis, "\nTahun Terbit: ", self.tahunTerbit)

    def umurBuku(self):
        return 2024 - self.tahunTerbit

    def hargaBuku(self):
        if self.jenis == "Fiksi":
            if self.umurBuku() > 50:
                return self.harga - self.harga * 10/100
            else:
                return self.harga - self.harga * 5/100
            
        if self.jenis == "Nonfiksi":
            if self.umurBuku() > 50:
                return self.harga - self.harga * 10/100
            else:
                return self.harga - self.harga * 2/100
            
        if self.umurBuku() > 50:
            return self.harga - self.harga * 10/100
        else:
            return self.harga

