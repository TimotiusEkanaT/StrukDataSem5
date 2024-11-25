class Mahasiswa:
    _nim=""
    _nama=""
    _ipk=0.0
                    
m = Mahasiswa
m._nim="1"
print(m._nim)

# class KartuKredit:
#     _noKartu=""
#     _namaPengguna=""
#     _limit=0.0
#     _saldo=0.0

#     def setNoKartu(self,noKartu):
#         self._noKartu = noKartu

#     def setNamaPengguna(self,nama):
#         self._namaPengguna = nama
#     def getNoKartu(self):
#         return self._noKartu
#     def getNamaPengguna(self):
#         return self._namaPengguna
    

## cara penggunaan:
# cc = KartuKredit()
# cc.setNoKartu("1")
# cc.setNamaPengguna("anton")
# print(cc.getNamaPengguna())
# print(cc.getNoKartu())


class KartuKredit:
    _noKartu=""
    _namaPengguna=""
    _limit=0.0
    _saldo=0.0
    def __init__(self,noKartu,namaPenguna,limit,saldo):
        self._noKartu = noKartu
        self._namaPengguna = namaPenguna
        self._limit = limit
        self._saldo = saldo
    def setNoKartu(self,noKartu):
        self._noKartu = noKartu
    def setNamaPengguna(self,nama):
        self._namaPengguna = nama
    def getNoKartu(self):
        return self._noKartu
    def getNamaPengguna(self):
        return self._namaPengguna
    def getLimit(self):
        return self._limit
    def getSaldo(self):
        return self._saldo

#cara penggunaan:
cc = KartuKredit("1","anton",10000,500)
#method di bawah ini dianggap ada
print(cc.getNamaPengguna())
print(cc.getNoKartu())
print(cc.getLimit())
print(cc.getSaldo())


