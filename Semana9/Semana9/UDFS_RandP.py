#UDFS R & P
class UFDSRP(object):
    def __init__(self, n):
        self.parent=[None]*n
        self.rank=[0]*n
        for x in range(0, n):
            self.parent[x]=int(x)
            #self.rank.append(0)

    def findParent(self, x):
        if(x==self.parent[x]):
            return x
        else:
            return self.findParent(self.parent[x])

    def findSet(self, u):
        if not u == self.parent[u]:
            self.parent[u] = self.findSet(self.parent[u]) #path compresion
        return self.parent[u]

    def isSameSet(self, x, y):
        return self.findParent(self.parent[x]) == self.findParent(self.parent[y])

    def Union(self, i, j):
        x = self.findSet(i)
        y = self.findSet(j)
        #self.isSameSet(i, j)
        if not(x == y):
            if(self.rank[x] > self.rank[y]):
                self.parent[y] = x
            else: 
                self.parent[x] = y
                if(self.rank[x]==self.rank[y]):
                    self.rank[y]+=1
            
#

#UDFS R
class UFDSR(object):
    def __init__(self, n):
        self.parent=[None]*n
        self.rank=[0]*n
        for x in range(0, n):
            self.parent[x]=int(x)
            #self.rank[x]=0

    def findParent(self, x):
        if(x==self.parent[x]):
            return x
        else:
            return self.findParent(self.parent[x])

    def isSameSet(self, x, y):
        return self.findParent(self.parent[x])==self.findParent(self.parent[y])


    def Union(self, x, y):
        i = self.findParent(x)
        j = self.findParent(y)
        if not(self.isSameSet(x, y)):
            if(self.rank[i] > self.rank[j]):
                self.parent[j] = i
            else: 
                self.parent[i] = j
                if(self.rank[i]==self.rank[j]):
                    self.rank[j]+=1

            
#


