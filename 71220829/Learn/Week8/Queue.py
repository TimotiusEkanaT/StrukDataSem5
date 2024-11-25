from Node import Node

class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def enqueue(self, e):
        if self.isEmpty():
            node_baru = Node(e, None)
            self._head = node_baru
            self._tail = node_baru
        else:
            node_baru = Node(e,None)
            self._tail._next = node_baru
            self._tail = node_baru
        self._size += 1

    def __str__(self):
        bantu = self._head
        hasil = '['
        while bantu != None:
            hasil += str(bantu._element) + ", "
            bantu = bantu._next
        hasil += ']'
        return hasil
    
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            hapus = self._head
            self._head = self._head._next
            self._size -= 1
            return hapus._element
    def first(self):
        if self.isEmpty():
            return None
        else:
            return self._head._element
        
    def last(self):
        if self.isEmpty():
            return None
        else: 
            return self._tail._element

def main():
    # arr = [20, 20, 10, 30]
    q = Queue()
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    print(q)
    q.dequeue()
    print(q)
    print(q.first())
    print(q.last())
    print(q)

if __name__ == "__main__":
    main()