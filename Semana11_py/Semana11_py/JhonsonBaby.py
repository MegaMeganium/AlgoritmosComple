MAX = 100
cost = [[None]*MAX for i in range(MAX)]
a = [[None]*MAX for i in range(MAX)]
def toInt(vec):
    for i in range(len(vec)):
        vec[i] = int(vec[i])
    #print(str(vec))
    return vec

def min(a,b):
    if a < b:
        return a
    return b

def read():
    fileW = open("outJ.txt","w")
    file = open("inputJ.txt","r")
    lines = file.readlines()
    lines = [x[:-1] for x in lines]
    file.close()
    test = int(lines[0])
    del lines[:1] #deleted index 1
    for nTest in range(test):
        n = int(lines[0].split(" ")[0])
        m = int(lines[0].split(" ")[1])
        Aristas = lines[1:1+m]
        Aristas = [toInt(x.split(" ")) for x in Aristas]
        for i in range(len(Aristas)):
            a[Aristas[i][0]][Aristas[i][1]] = Aristas[i][2]
        print(str(a))
        for i in range(n):
            for j in range(n):
                if a[i][i] == 0 and i!=j:
                    a[i][j] = 99999
        print(str(a))
        for k in range(n):
           for i in range(n):
               for j in range(n):        
                    a[i][j] = min(a[i][j],a[i][k]+a[k][j])
        
        fileW.write("Resultante \tmatriz de adyacencia\n")
        for i in range(n):
            for j in range(n):
                if a[i][j] != 99999:
                    fileW.write(str(a[i][j])+" ")
            print("\n")
    del lines[:1+m+1]
    fileW.close()
        
def control():
    a=1
    