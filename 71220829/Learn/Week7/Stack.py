from Node import Node

class Stack:
    def __init__(self) -> None:
        self._head = None
        self._size = 0

    def __len__ (self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0
    
    def push(self, element):
        nodeBaru = Node(element, None)
        if self.isEmpty():
            self._head = nodeBaru
            self._head._next = None
        else:
            nodeBaru._next = self._head
            self._head = nodeBaru
        self._size += 1

    def top(self):
        if self.isEmpty():
            return "stack kosong"
        else:
            return self._head._element
        
    def pop(self):
        if self.isEmpty():
            print("stack kosong")
        else:
            element = None
            if self._head._next == None:
                # element = self._head._element
                self._head = None
            else:
                # element = self._head._element
                self._head = self._head._next
            return element
        
    def printAll(self):
        if self.isEmpty():
            return "stack kosong"
        else:
            bantu = self._head
            while (bantu != None):
                print(bantu._element, " ", end="")
                bantu = bantu._next
                print()