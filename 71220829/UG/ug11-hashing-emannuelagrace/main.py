class HashTable:
    def __init__(self):
        self.size = 10
        self.map = [None]*self.size
    
    def _get_hash(self, key):
        return key % self.size
    
    def _linear_probing(self, key, index):
        return (self._get_hash(key) + index) % self.size
    def _probing(self, key):
        for index in range(self.size):
            probeHash = self._linear_probing(key, index)
            if self.map[probeHash] is None or self.map[probeHash] == 'deleted':
                return probeHash
        return None
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        
        if self.map[key_hash] is None:
            self.map[key_hash] = key_value
        else:
            new_hash = self._probing(key)
            if new_hash is not None:
                self.map[new_hash] = key_value
            else:
                print("Hash table penuh!")
    def print_all(self):
        print("==== ISI HASH TABLE ====")
        for item in self.map:
            if item is not None and item != 'deleted':
                print(f"NIM: {item[0]} NAMA: {item[1]}")
    
    def get_data(self, key):
        for index in range(self.size):
            probeHash = self._linear_probing(key, index)
            if self.map[probeHash] is None:
                return None
            if self.map[probeHash][0] == key:
                return self.map[probeHash][1]
        return None
    def resize(self, size):
        mapLama = self.map
        self.size = size
        self.map = [None] * self.size
        for item in mapLama:
            if item is not None and item != 'deleted':
                self.add(item[0], item[1])


def main():
    ht : HashTable = HashTable()
    # isi hash table
    ht.add(71210689, "Gian")
    ht.add(71210683, "Yandi")
    ht.add(71210699, "Andreas")

    print("==== HASH TABLE SEBELUM DIRESIZE ====")
    print()
    ht.print_all()
    print(f"mahasiswa dengan NIM 71210683 adalah {ht.get_data(71210683)}")
    print()
    # resize hash table
    ht.resize(3)

    print("==== HASH TABLE SETELAH DIRESIZE ====")
    print()
    ht.print_all()
    print(f"mahasiswa dengan NIM 71210683 adalah {ht.get_data(71210683)}")
    

if __name__ == "__main__":
    main()