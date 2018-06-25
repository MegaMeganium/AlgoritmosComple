// Karger_cmas.cpp : main project file.

#include "stdafx.h"

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
using namespace std;
using namespace System;
class Edge {
public:
	int src;
	int dest;

};

class Graph {
public:
	int n, m;
	Edge* edge;
};

class Set {
public:
	int parent;
	int rank;
};

int find(Set* sets, int i) {
	if (sets[i].parent != i)
		sets[i].parent = find(sets, sets[i].parent);
	return sets[i].parent;
}

void Union(Set* sets, int x, int y) {
	int px = find(sets, x);
	int py = find(sets, y);

	if (sets[px].rank < sets[py].rank)
		sets[py].parent = py;
	else if (sets[px].rank > sets[py].rank)
		sets[py].parent = px;
	else {
		sets[py].parent = px;
		sets[px].rank++;
	}
}

int kargerMinCut(Graph* graph) {
	int V = graph->n;
	int E = graph->m;
	Edge*edge = graph->edge;
	Set* sets = new Set[V];

	for (int n = 0; n < V; n++) {
		sets[n].parent = n;
		sets[n].rank = 0;
	}

	int vertices = V;

	while (vertices > 2) {
		int i = rand() % E;
		int set1 = find(sets, edge[i].src);
		int set2 = find(sets, edge[i].dest);

		if (set1 == set2)
			continue;
		else {
			printf("Contract the edges: %d <->%d\n", edge[i].src, edge[i].dest);
			vertices--;
			Union(sets, set1, set2);
		}

	}
	int cutedges = 0;

	for (int m = 0; m< E; m++)
	{
		int set1 = find(sets, edge[m].src);
		int set2 = find(sets, edge[m].dest);
		if (set1 != set2)
			cutedges++;
	}
	return cutedges;

}

Graph* createGraph(int V, int E)
{
	Graph* graph = new Graph;
	graph->n = V;
	graph->m = E;
	graph->edge = new Edge[E];
	return graph;

}

int main() {
	int n, m, cases;
	int u, v;
	srand(time(NULL));

	freopen("in.txt", "rt", stdin);
	freopen("outt.txt", "wt", stdout);

	scanf("%d", &cases);
	while (cases-- > 0) {
		scanf("%d %d", &n, &m);
		Graph* graph = createGraph(n, m);
		for (int i = 0; i < m; i++)
		{
			scanf("%d %d", &u, &v);
			graph->edge[i].src = u;
			graph->edge[i].dest = v;
		}

		printf("\nMinimun Cut is=> %d\n", kargerMinCut(graph));
	}

	return 0;

}
