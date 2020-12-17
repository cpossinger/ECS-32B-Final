from collections import defaultdict



"""
BFS
"""
def bfs(map, office):
    graph_dict = defaultdict(list)
    visited_dict = {}
    path_dict = defaultdict(list)
    pred_dict = {}

    for u,v in map:
        graph_dict[u].append(v)
        visited_dict[u] = False
    pred_dict[office] = None
    for i in list(graph_dict.keys())[1:]:
        pred_dict[i] = graph_dict[i][0]

    queue = []
    queue.append(office)
    visited_dict[office] = True
    while queue:
        current_stop = queue.pop(0)
        current_pred = current_stop
        while True:
            if current_pred != office:
                path_dict[current_stop].append(current_pred)
                current_pred = pred_dict[current_pred]
            else:
                path_dict[current_stop].append(office)
                break
        for i in graph_dict[current_stop]:
            if visited_dict[i] == False:
                queue.append(i)
                visited_dict[i] = True
    for i in path_dict.keys():
        path_dict[i].reverse()
    return path_dict





map = [("ups","b"),("ups","c"),("b","ups"),("b","c"),("b","d"),("c","ups"),("c","b"),("c","d"),("d","b"),("d","c")]
print(bfs(map,"ups"))





"""
DFS
"""
def dfs(map, office):
    graph_dict = defaultdict(list)
    visited_set = set()
    for u, v in map:
        graph_dict[u].append(v)

    return dfsHelper(graph_dict,visited_set,office)



def dfsHelper(graph_dict,visited_set,current_stop):
    if visited_set == len(graph_dict.keys()):
        return visited_set
    visited_set.add(current_stop)
    for i in graph_dict[current_stop]:
        if i not in visited_set:
           return dfsHelper(graph_dict,i,visited_set)


map = [("ups", "b"), ("ups", "c"), ("c", "ups"), ("c", "b"), ("c", "d"), ("b", "ups"), ("b", "c"), ("b", "d"),("d", "c"), ("d", "b")]
print(dfs(map, "ups"))


"""
Dijkstra's
"""
def dijkstra(map, office):


def minDistance(self, dist, sptSet):

        # Initilaize minimum distance for next node
        min = sys.maxsize

        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

        # Funtion that implements Dijkstra's single source
        # shortest path algorithm for a graph represented
        # using adjacency matrix representation

    def dijkstra(self, src):

        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for cout in range(self.V):

            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)

            # Put the minimum distance vertex in the
            # shotest path tree
            sptSet[u] = True

            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shotest path tree
            for v in range(self.V):
                if self.graph[u][v] > 0 and \
                        sptSet[v] == False and \
                        dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.printSolution(dist)


map = [("ups", "b"), ("ups", "c"), ("c", "ups"), ("c", "b"), ("c", "d"), ("b", "ups"), ("b", "c"), ("b", "d"),("d", "c"), ("d", "b")]
print(dijkstra(map, "ups"))

