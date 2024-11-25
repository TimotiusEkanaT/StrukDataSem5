class Restoran:
    def __init__(self):
        self.size = 5
        self.map = [None] * self.size

    def _getHash(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char) # mendapatkan nilai ASCII
        return hash % self.size

    def _probing(self, key):
        for index in range(self.size):
            # probeHash = (self._getHash(key)+index) % self.size
            probeHash = self._linearProbing(key, index)
            # valid bila index adalah None atau ber-flag deleted
            if (self.map[probeHash] is None) or (self.map[probeHash] == 'deleted'):
                return probeHash

    # melakukan linear probing
    def _linearProbing(self, key, index):
        return (self._getHash(key)+index) % self.size

    # menambahkan key pada hash table
    def tambahReservasi(self, key, value):
        key_hash = self._getHash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            key_hash = self._probing(key)
            if(key_hash is None):
                print("Reservasi sudah penuh")
                return False
            
            self.map[key_hash] = list([key_value])
            return False

    def lihatReservasi(self, key):
        key_hash = self._getHash(key)
        for index in range(self.size):
            probeHash = self._linearProbing(key, index)
            if self.map[probeHash] is None:
                return "None"
            if self.map[probeHash][0][0] == key:
                return self.map[probeHash][0][1]
        return "None"
        

    def reserveDone(self, key):
        key_hash = self._getHash(key)
        if self.map[key_hash] is None:
            return False
        for index in range(self.size):
            #menghapus dengan melakukan linear probing
            key_hash = self._linearProbing(key, index)
            # periksa apakah key adalah data yg akan dihapus
            if(self.map[key_hash][0][0] == key):
                print("deleting ", key)
                self.map[key_hash] = "deleted"
                return True
            
        print("Key ", key, " tidak ditemukan")
        return False

    def printAll(self):
        print('--Reservasi--')
        for item in self.map:
            if item is not None:
                print(str(item))

if __name__ == "__main__":
    rak1 = Restoran()

    rak1.tambahReservasi("Draine", "Family Dinner")
    rak1.tambahReservasi("Perry", "Birthday Party")
    rak1.tambahReservasi("Octo", "Romantic Dinner")
    rak1.tambahReservasi("Peter", "Lunch")
    rak1.tambahReservasi("Hrain", "Test Food Wedding")
    rak1.tambahReservasi("Gura", "Garden Party")
    
    print(rak1.lihatReservasi("Octo"))
    print(rak1.lihatReservasi("Buna"))

    rak1.reserveDone("Pery")
    rak1.reserveDone("Draine")
    rak1.printAll()
