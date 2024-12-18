from Node import Node

class SLLNC: #Single Linked List non Circular (List yang tidak memiliki loop atau ketika sudah mencapai tail, maka selesai)
    def __init__(self):
        self._head=None
        self._tail=None
        self._size = 0

    def __len__(self):
        return self._size

    def isEmpty(self):
        return self._size == 0

    def addElementHead(self,element):
        baru = Node(element, None)
        if self.isEmpty()==True:
            self._head = baru
            self._tail = baru
            self._tail._next = None #Sebenarnya Next tail sudah pasti none
        else:
            baru._next = self._head
            self._head = baru
        self._size += 1
        print("Data",element, "masuk head!")

    def addElementTail(self,element):
        baru = Node(element, None)
        if self._tail == None:
            self._head = baru
            self._tail = baru
            self._tail._next = None
        else:
            self._tail._next = baru
            self._tail = baru
        self._size += 1
        print("Data",element, " masuk tail!")

    def deleteFirst(self):
        if self.isEmpty()==False:
            d = ""
            if self._head._next==None:
                d = self._head._element
                self._head=None
                self._tail=None
            else:
                hapus = self._head
                d = hapus._element
                self._head = self._head._next
                hapus._next=None
                del hapus
            self._size -= 1
            print(d," terhapus!")
        else:
            print("Kosong!")


    def deleteLast(self):
        if self.isEmpty() == False:
            d = None
            bantu = self._head
            if(self._head != self._tail):
                while bantu._next != self._tail:
                    bantu = bantu._next
                hapus = self._tail
                self._tail = bantu
                d = hapus._element
                del hapus
                self._tail._next = None
            else:
                d = self._tail._element
                self._head=None
                self._tail=None
            self._size -= 1
            print(d, " terhapus!")
        else:
            print("Kosong!")

    def printAll(self):
        if self.isEmpty()==False:
            bantu = self._head
            while(bantu!=None):
                print(bantu._element," ",end='')
                bantu = bantu._next
            print()
        else:
            print("Kosong")