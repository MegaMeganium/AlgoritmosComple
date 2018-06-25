from sys import maxsize as maxInt

class Struct(object):
    def __init__(self,u,v,w):
        self.u=u
        self.v=v
        self.w=w

def showVectors(vec):
    print("\n")
    for obj in vec:
        print(str(obj)+"\n")

def BellmanFord(edges, nNodos, source):
    d = [maxInt for i in range(nNodos)]
    d[source] = 0
    #print(str(nNodos)+", "+str(edges))
    for i in range(nNodos-1):
        for j in range(len(edges)):
            if d[edges[j].u] + edges[j].w < d[edges[j].v]:
                d[edges[j].v] = d[edges[j].u] + edges[j].w

    for i in range(nNodos-1):
        for j in range(len(edges)):
            if d[edges[j].u] + edges[j].w < d[edges[j].v]:
                print("Negative cycle\n")
    print(str(d))
    return d

def read():
    file = open("in.txt", "r")
    lines = file.readlines()
    file.close()
    lines = [i[:-1] for i in lines]
    lines = [x.split(" ") for x in lines]
    print(str(lines))
    edges = [] #nAristas
    for i in range(len(lines)):
        for j in range(len(lines)):
            if not int(lines[i][j]) == 0:
                edges.append(Struct(i,j,int(lines[i][j])))
    #for gr in edges:
        #print(str(gr.u)+", "+str(gr.v)+", "+str(gr.w))
    edges.append(len(lines)) #nNodos
    return edges

def write(d):
    file = open("out.txt", "w")
    file.write("\nNode\tDistancia\n")
    file.write("----\t--------\n")
    for i in range(len(d)):
        file.write(str(i)+"\t\t\t"+str(d[i])+"\n")
    file.close()

def control():
    edges = read()
    nNodos = edges[len(edges)-1]
    del edges[-1:] #se borra el ultimo index
    d = BellmanFord(edges, nNodos, 0)
    write(d)