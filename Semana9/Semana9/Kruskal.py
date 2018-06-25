from UDFS_RandP import *
class Kruskal(object):
    def __init__(self):
        self.readFile = "input.txt"
        self.outFile = "output.txt"
        self.read()
        #print(str(self.nNode) +", "+str(self.nArist))
        self.ufds = UFDSRPv2(self.nNode)

    def read(self):
        file = open("input.txt", "r")
        lines = file.readlines()
        file.close()
        lines = [x[:-1] for x in lines]
        self.nCases = int(lines[0])
        print(lines)
        self.nNode = int(lines[1].split(" ")[0])
        self.nArist = int(lines[1].split(" ")[1])
        
        del lines[:2] #delete 2 first elemnts index(0,1)
        self.lines = [x.split(" ") for x in lines]
        #self.lines = [[int(x[0]), int(x[0]), int(x[0])] for x.split(" ") in lines]
        print(self.lines)
        self.lines = [[int(i[0]), int(i[1]), int(i[2])] for i in self.lines]
        print(self.lines)
        self.lines.sort(key = lambda x: x[2])
        print(self.lines)

    def Union(self):
        for line in self.lines:
            self.ufds.Union(line[0], line[1])
            print(str(line[0]) +", "+ str(line[1]))

    def write(self):
        file = open(self.outFile, "w")
        file.write(str(self.ufds.parent)+"\n")
        file.write(str(self.ufds.rank))
        print(str(self.ufds.parent))
        print(str(self.ufds.rank))
        file.close()


