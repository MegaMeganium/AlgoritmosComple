#import queue as Q
import sys
class MinHeap(object):

    def __init__(self):
        self.Heap = [None]
        #el arreglo tiene el root en index = 1
    @staticmethod
    def Parent(i):
        return int(i / 2)
    @staticmethod
    def LeftChild(i):
        return int(2 * i)
    @staticmethod
    def RighChild(i):
        return int(2 * i + 1)

    def Insert(self, v):
        self.Heap.append(v)
        i = len(self.Heap) - 1
        parent = MinHeap.Parent(i)

        if i > 1 and self.Heap[parent] < self.Heap[i]:
            self.Heap[i], self.Heap[parent] = self.Heap[parent], self.Heap[i]
        self.HeapSort()

    def Crear(self, cadena):
        vec = cadena[:-1].split(",")
        #vec = [2,7,26,25,19,17,1,90,3,36]
        for i in vec:
            self.Insert(int(i))

    def show(self):
        for x in range(1, len(self.Heap)):
            print("Heap[" + str(x) + "]=> " + str(self.Heap[x]) + " :p-> " + str(self.Heap[MinHeap.Parent(x)]))

    def ExtractMax(self):
        self.Swap(1, len(self.Heap) - 1)
        self.Heap.remove(self.Heap[len(self.Heap) - 1])
        self.HeapSort()

    def ExtractKey(self, key):
        if key >= len(self.Heap):
            return
        self.Heap[key] = sys.maxsize #el int maximo
        self.Swap(1, key)
        self.ExtractMax()
    
    def Swap(self, a , b):
        self.Heap[a], self.Heap[b] = self.Heap[b], self.Heap[a]

    def HeapSort(self):
        for i in range(1, len(self.Heap)):
            LC = MinHeap.LeftChild(i)
            RC = MinHeap.RighChild(i)
            parent = MinHeap.Parent(i)

            if LC < len(self.Heap) and self.Heap[LC] > self.Heap[i]:
                self.Swap(LC, i)

            if RC < len(self.Heap) and self.Heap[RC] > self.Heap[i]:
                self.Swap(RC, i)

            if i > 1 and self.Heap[parent] < self.Heap[i]:
                self.Swap(parent, i)