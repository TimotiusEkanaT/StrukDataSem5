class BukuTelepon:
    def __init__(self):
        self.size = 6
        self.map = [None] * self.size

    def _getHash(self, key):
        hash = 0
        for char in str (key):
            hash += ord(char) #mendapatkan nilai ASCII
        return hash % self.size
    
    def _probing(self, key):
        for index in range (self.size):
            probeHash = self._linearProbing(key, index)
            if (self.map[probeHash] is None) or (self.map[probeHash] == 'deleted'):
                return probeHash
            
    def _linearProbing(self, key, index):
        return(self._getHash(key)+index) % self.size

    def add(self, key, value):
        key_hash = self._getHash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            key_hash = self._probing(key)
            if(key_hash is None):
                print("Buku telepon sudah penuh")
                return False
            
            self.map[key_hash] = list([key_value])
            return False
        
    def getPhoneNumber(self, key):
        key_hash = self._getHash(key)
        for index in range(self.size):
            probeHash = self._linearProbing(key, index)
            if self.map[probeHash] is None:
                return "None"
            if self.map[probeHash][0][0] == key:
                return self.map[probeHash][0][1]
        return "None"

        
    def delete(self, key):
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
    
    def print(self):
        print('---Buku Telepon---')
        for item in self.map:
            if item is not None:
                print(str(item))



h = BukuTelepon()
h.add('Dendy', '567-8888')
h.add('Yuan', '293-6753')
h.add('Anton', '333-8233')
h.add('Adi', '293-8625')
h.add('Dida', '293-8625')
h.add('Didasdas', '293sadsda-8625')
h.print()
h.delete('Dida')
h.print()
h.add('Ddasd', '293-86a')
h.print()
print('Anton: ' + h.getPhoneNumber('Anton'))