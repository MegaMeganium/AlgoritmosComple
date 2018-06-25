def toInt(vec):
    for i in range(len(vec)):
        vec[i] = int(vec[i])
    print(str(vec))
    return vec
class Struct(object):
    def __init__(self, N, R, Aristas, u, v):
        self.N = N #nVertices
        self.R = R #nAristas
        self.graph = [[None]*N for i in range(N)]
        Aristas = [toInt(x.split(" ")) for x in Aristas]
        print("\n\n"+str(Aristas)+"\n")
        #Aristas = [ al.append(int(x)) for arista in Aristas for x in arista]
        #print("\n\n"+str(Aristas)+"\n")

        for arista in Aristas:
            self.graph[int(arista[0])][int(arista[1])] = int(arista[2])

        for i in range(0, N):
            for j in range(0, N):
                if i == j:
                    self.graph[i][j] = 0
                elif self.graph[i][j] == None:
                    self.graph[i][j] = 99999
        self.u = u
        self.v = v

        for obj in self.graph: 
            print(str(obj)+"\n")
#
def read():
    file = open("input.txt", "r")
    lines = file.readlines()
    file.close()
    lines = [x[:-1] for x in lines]
    #print(str(lines))
    T = int(lines[0]) #nCasos
    cases = [None]*T
    del lines[:2] #deleted index 0, 1 (T, "")
    for nCase in range(T):
        N = int(lines[0])
        R = int(lines[1])
        Aristas = lines[2:2+R]
        #print("\ntest: "+str(lines[2+R:2+R+1][0].split(" "))+"\n")
        UV = lines[2+R:2+R+1][0].split(" ")
        cases[nCase] = Struct(N, R, Aristas, int(UV[0]), int(UV[1]))
        del lines[:2+R+1+1]

    return cases

def write(graph):
    file = open("output.txt", "w")
    for obj in graph:
        file.write(str(obj) + "\n")
    file.close()

def writeCases(cases):
    file = open("output.txt", "w")
    for case in cases:
        for vec in case.graph:
            file.write(str(vec) + "\n")
        file.write("\n\n")
    for case in cases:
        file.write("Caso "+str(cases.index(case)+1)+": "+str(case.graph[case.u][case.v])+"\n")
    file.close()

def flodWarshell(graph, N):
    #dist = [[None]*N]*N #hacer esto esta mal
    dist = graph

    for k in range(0, N):
        for i in range(0, N):
            for j in range(0, N):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    for obj in dist: 
        print(str(obj))
    print("\n")

    return dist
    
def control():
    cases = read()
    for case in cases:
        case = flodWarshell(case.graph, len(case.graph))
    writeCases(cases)
    
