class Node:
    def __init__(self, value):
        self.next = None
        self.data = value

class SLNC:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def getLength(self):
        return self.size

    def writeAllData(self):
        if self.size == 0:
            result = 'Linked list kosong'
        else:
            result = 'Linked List: ' + str(self.size) + ' data: \n'
            helper = self.head
            while helper != None:
                result = result + str(helper.data) + ' '
                helper = helper.next
        print(result)

    # methods
    def insert_head(self, new_data):
        node_baru = Node(new_data)
        if self.size == 0:
            self.head = node_baru
            self.tail = node_baru
        else:
            node_baru.next = self.head
            self.head = node_baru
        self.size = self.size + 1
    
    def insert_tail(self, new_data):
        node_baru = Node(new_data)
        if self.size == 0:
            self.head = node_baru
            self.tail = node_baru
        else:
            self.tail.next = node_baru
            self.tail = node_baru

        self.size = self.size + 1
    
    def insert_mid(self, new_data, index):
        if self.size == 0 or index <= 0:
            self.insert_head(new_data)
        elif index >= self.size:
            self.insert_tail(new_data)
        else:
            node_baru = Node(new_data)
            helper = self.head
            for i in range(index-1):
                helper = helper.next
            node_baru.next = helper.next
            helper.next = node_baru
            self.size = self.size + 1
    def delete_head(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            deleted_node = self.head
            self.head = None
            self.tail = None
            self.size = self.size - 1
            return deleted_node
        else:
            hapus = self.head
            deleted_node = self.head
            self.head = self.head.next
            del hapus
            self.size = self.size - 1
            return deleted_node
            
    def delete_tail(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            deleted_node = self.head
            self.head = None
            self.tail = None
            self.size = self.size - 1
            return deleted_node
        else:
            helper = self.head
            while helper.next != self.tail:
                helper = helper.next
            hapus = self.tail
            deleted_node = self.tail
            self.tail = helper
            self.tail.next = None
            del hapus
            self.size = self.size - 1
            return deleted_node

    def delete_mid(self, index):
        if self.size == 0 or index <= 0:
            return self.delete_head()
        elif index >= self.size-1:
            return self.delete_tail()  
        else:
            helper = self.head
            for i in range(index-1):
                helper = helper.next
            hapus = helper.next
            helper.next = hapus.next
            deleted_node = hapus
            del hapus
            self.size = self.size - 1
            return deleted_node

    """
    Method getData(self, index) akan mereturn data dari linked list berdasarkan
    parameter index. Cara kerjanya hampir sama seperti index pada
    list biasa.
    """
    def getData(self, index) :
        helper = self.head
        for i in range(index-1):
            helper = helper.next
        result = helper.next
        return result.data

        

    def hapusDuplikasi(self):
        # a = 1
        # result = None
        # while self.size !=0:
        #     if self.getData(a-1) == (self.getData(a)):
        #         b = self.getData(a)
        #         del b
        #         a += 1
        #     else:
        #         result = a
        a = None
        for i in range (0, self.size):
            a = self.getData(i)
            ll = SLNC()
            for j in range(i, self.size):
                if a == self.getData(j):
                    break
            else:
                ll.insert_tail(a)
        
        self.head = ll.head
        self.tail = ll.tail
        self.size = ll.size
            







if __name__ == "__main__":
    ll = SLNC()
    for i in [1, 1, 1, 1, 1, 2, 3, 4, 2, 2, 2, 5, 6]:
        ll.insert_tail(i)
    ll.writeAllData()
    ll.hapusDuplikasi()
    ll.writeAllData()
    # print(ll.getData(2))