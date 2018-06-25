import sys
from UDFS_RandP import UFDSRP as UDFS_R_P
from BinaryHeaps import MinHeap
from Kruskal import Kruskal

def UDFS_main():
    obj = UDFS_R_P(8)
    obj.Union(0, 3)
    obj.Union(1, 3)
    obj.Union(2, 3)
    obj.Union(4, 3)
    obj.Union(5, 6)
    obj.Union(7, 6)
    obj.Union(3, 6)
    print(obj.parent)
    print(obj.rank)

#UDFS_main()

def MinHeap_main():
    obj = MinHeap()
    #print("Heap = ", end = '', flush = True)
    print("Heap = ")
    obj.Crear(sys.stdin.readline())
    obj.show()
    obj.Insert(8)
    obj.Insert(20)
    obj.Insert(100)
    print("\n")
    obj.show()
    #obj.ExtractMax()
    #obj.show()
    #print(obj.Heap)
    #obj.ExtractKey(4)
    #obj.show()

MinHeap_main()

def prueba():
    lst = [1,2,3,4,5]
    #del lst[2:4] #delet since 2 until 4-1
    del lst[:2] #delete first tow elemetes
    print(lst)
    string = ["12", "34"]
    string = [x[:-1] for x in string] 
    print(string)

#prueba()

def Kruskal_main():
    obj = Kruskal()
    obj.Union()
    obj.write()

#Kruskal_main()