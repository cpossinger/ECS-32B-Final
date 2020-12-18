from collections import defaultdict
import sys



"""
BFS
"""
def bfs(map, office):
    print(map)
    print(office)
    graph_dict = defaultdict(list)
    visited_dict = {}
    path_dict = defaultdict(list)
    pred_dict = {}

    for u,v,w in map:
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





map = [("UPS","Brecon",3),("Jacob City","Owl Ranch",3),("Jacob City","Sunfield",15),("Sunfield","Brecon",25)]
print(bfs(map,"ups"))





"""
DFS
"""
def dfs(map, office):
    print(map)
    print(office)
    graph_dict = defaultdict(list)
    visited_set = set()
    for u, v,w in map:
        graph_dict[u].append(v)

    return dfsHelper(graph_dict,visited_set,office)



def dfsHelper(graph_dict,visited_set,current_stop):
    if visited_set == len(graph_dict.keys()):
        return visited_set
    visited_set.add(current_stop)
    for i in graph_dict[current_stop]:
        if i not in visited_set:
           return dfsHelper(graph_dict,i,visited_set)


map = [("UPS","Brecon",3),("Jacob City","Owl Ranch",3),("Jacob City","Sunfield",15),("Sunfield","Brecon",25)]
print(dfs(map, "ups"))


"""
Dijkstra's
"""
def dijkstra(map, office):
    print(map)
    print(office)
    graph_dict = defaultdict(list)
    dist = {}
    pred_dict = {}
    dist[office] = 0
    for u,v,w in map:
        graph_dict[u].append(v)
        pred_dict[u] = None
    for i in list(graph_dict.keys())[1:]:
        dist[i] = sys.maxsize






map = [("UPS","Brecon",3),("Jacob City","Owl Ranch",3),("Jacob City","Sunfield",15),("Sunfield","Brecon",25)]
print(dijkstra(map, "ups"))

