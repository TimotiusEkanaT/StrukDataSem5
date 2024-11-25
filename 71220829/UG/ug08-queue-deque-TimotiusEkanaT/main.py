class Queue :
    def __init__(self):
        self.data = []
    
    def enqueue(self, data) :
        self.data.append(data)

    def dequeue(self):
        if len(self.data) == 0:
            return
        else :
            return self.data.pop(0)

    def front(self):
        if len(self.data) == 0 :
            return 
        else :
            return self.data[0]
    
    def get_length(self) :
        return len(self.data)

    def write_all_data(self):
        print("DATA: ")
        for i, data in enumerate(self.data):
            print(f"{data}")



# Haram untuk menggunakan list
def get_min(queue):
    q = Queue()
    b = None
    lenbantu = queue.get_length()
    lenbantu2 = queue.get_length()
    while lenbantu != 0:
        a = queue.dequeue()
        q.enqueue(a)
        a = queue.enqueue(a)
        lenbantu -= 1

    while lenbantu2 != 0 :
        c = q.dequeue()
        if b == None:
            b = c
        else:
            if c < b:
                b = c
            else:
                b = b
        lenbantu2-=1
    return b



def pop(queue):
    q = Queue()
    lenbantu = queue.get_length()
    lenbantu2 = queue.get_length()
    while lenbantu != 1:
        a = queue.dequeue()
        q.enqueue(a)
        lenbantu -= 1  
    while lenbantu != lenbantu2:
        a = q.dequeue()
        queue.enqueue(a)
        lenbantu += 1
    z =  queue.front()
    queue.dequeue()
    return z


if __name__ == "__main__":
    q : Queue = Queue()
    for i in [10, 8, 5, 60,1,2,3,4,100]:
        q.enqueue(i)
    print("==========")
    print("Data Awal")
    q.write_all_data()
    print("==========")
    print(f"Data terkecil = {get_min(q)}")
    print("==========")
    print()
    print("Pembuktian isi queue tidak berubah")
    print("==========")
    print("Data Akhir")
    q.write_all_data()
    print("==========")
    print()
    print("============")
    print("Percobaan Pop")
    print(f"pop - 1 = {pop(q)}")
    print(f"pop - 2 = {pop(q)}")
    print(f"pop - 3 = {pop(q)}")
    print("=============")
    print("Hasil Akhir: ")
    q.write_all_data()
    print("=============")
