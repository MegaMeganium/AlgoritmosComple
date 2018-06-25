import FlodWarshell as FD
import Bellmanford as BF
import JhonsonBaby as JB

def main():
    INF = 99999
    graph = [
			    [0,5,INF,10],
				[INF,0,3,INF],
				[INF,INF,0,1],
				[INF,INF,INF,0]
			]

    de = [
            "123",
            "24",
            "54",
            "568"
         ]
    #del de[-1:]
    #print(str(de[:-1])+"\n")

    #FD.control()
    #BF.control()
    JB.read()

main()
