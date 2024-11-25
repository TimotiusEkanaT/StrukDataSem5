def mergesort(data):
    if len(data)>1:
        mid = len(data)//2
        left = data [:mid]
        right = data [mid:]

        mergesort(left)
        mergesort(right)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i][1] >= right [j][1]:
                data[k] = left[i]
                i += 1
            else:
                data[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1

class PriorityQueueSorted:
    def __init__(self):
        self.data = []

    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
        
    def len(self):
        return len(self.data)
        
    
    def print_all(queue):
        print(queue.data)

    def remove(self):
        if self.is_empty() == False:
            del self.data[0]

    def peek(self):
        if self.is_empty() == True:
            return None
        else:
            return self.data[0]

    def add(self, data, priority):
        baru = [data,priority]
        self.data.append(baru)
        mergesort(self.data)


myQueue = PriorityQueueSorted()

myQueue.add('Gian', 2)

myQueue.add('Kezia', 8)

myQueue.print_all()

myQueue.peek()

myQueue.add('Glen', 5)

myQueue.add('Christo', 9)

myQueue.print_all()

myQueue.peek()

print("========REMOVE========")

myQueue.remove()

myQueue.print_all()

myQueue.remove()

myQueue.print_all()

myQueue.remove()

myQueue.print_all()

myQueue.add('Saya', 7)

myQueue.print_all()