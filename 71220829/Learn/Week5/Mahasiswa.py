class Mahasiswa:
    # _nim=""
    # _nama=""
    # _ipk=0.0


    # Construction
    def __init__(self, nim = None, nama = None, ipk = None):
        self.nim = nim
        self.nama = nama
        self.ipk = ipk
    
    #Method
    # def setNama(self, nama):
    #     self._nama = nama

    # def setNim(self, nim):
    #     self._nim = nim

    # def setIpk(self, ipk):
    #     self._ipk = ipk

    # def getNama(self):
    #     return self._nama
    
    # def getNim(self):
    #     return self._nim
    
    # def getIpk(self):
    #     return self._ipk
    
    def registrasiMataKuliah(self):
        print("Mahasiswa ", self._nama, " melakukan registrasi")

    def menggunakanLabKomputer(self):
        print("Mahasiswa ", self._nama, " menggunakan Lab Komputer")
