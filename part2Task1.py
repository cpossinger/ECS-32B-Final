from collections import defaultdict
import sys



"""
BFS
"""
def bfs(map, office):
    graph_dict = defaultdict(list)
    visited_dict = {}
    path_dict = defaultdict(list)
    pred_dict = {}

    for u,v,w in map:
        graph_dict[u].append(v)
        graph_dict[v].append(u)
        visited_dict[u] = "Unvisited"
        visited_dict[v] = "Unvisited"
    queue = []
    queue.append(office)
    visited_dict[office] = "Visited"
    pred_dict[office] = []
    while queue:
        current_stop = queue.pop(0)
        path_dict[current_stop] = getPath(office,current_stop,[],pred_dict)
        for i in graph_dict[current_stop]:
            if visited_dict[i] == "Unvisited":
                queue.append(i)
                pred_dict[i] = current_stop
                visited_dict[i] = "Visiting"
        visited_dict[current_stop] = "Visited"
    for i in path_dict.keys():
        path_dict[i].reverse()

    return path_dict


def getPath(office,current_pred,path,pred_dict):
    if current_pred == office:
        return path + [office]
    path.append(current_pred)
    return getPath(office,pred_dict[current_pred],path,pred_dict)





# map =  [('UPS', 'Steuben', 22), ('Richmond Hill', 'Steuben', 20), ('Richmond Hill', 'Hambleton', 17), ('Richmond Hill', 'Owl Ranch', 25),
#         ('Holly Ridge', 'Diehlstadt', 0),
#         ('Holly Ridge', 'Jacob City', 0), ('Holly Ridge', 'Steuben', 17), ('Diehlstadt', 'Brecon', 8), ('Diehlstadt', 'Hambleton', 9),
#         ('Diehlstadt', 'Steuben', 11),("Steuben","Hambleton",13), ('Steuben', 'Brecon', 25), ('Hambleton', 'Jacob City', 1), ('Jacob City', 'Sunfield', 19),
#         ('Jacob City', 'Brecon', 1), ('Sunfield', 'Brecon', 12)]
# print(bfs(map,"UPS"))





"""
DFS
"""


def dfs(map, office):
    graph_dict = defaultdict(list)
    visited_dict = {}
    path_dict = defaultdict(list)
    pred_dict = {}

    for u,v,w in map:
        graph_dict[u].append(v)
        graph_dict[v].append(u)
        visited_dict[u] = False
        visited_dict[v] = False
    stack = []
    stack.append(office)
    visited_dict[office] = True
    pred_dict[office] = None
    while stack:
        current_stop = stack.pop()
        path_dict[current_stop] = getPath(office,current_stop,[],pred_dict)
        for i in graph_dict[current_stop]:
            if visited_dict[i] == False:
                stack.append(i)
                pred_dict[i] = current_stop
                visited_dict[i] = True
    for i in path_dict.keys():
        path_dict[i].reverse()
    return path_dict


def getPath(office,current_pred,path,pred_dict):
    if current_pred == office:
        return path + [office]
    path.append(current_pred)
    return getPath(office,pred_dict[current_pred],path,pred_dict)








# def dfs(map, office):
#     print(map)
#     print(office)
#     graph_dict = defaultdict(list)
#     visited_set = set()
#     for u, v,w in map:
#         graph_dict[u].append(v)
#
#     return dfsHelper(graph_dict,visited_set,office)
#
#
#
# def dfsHelper(graph_dict,visited_set,current_stop):
#     if visited_set == len(graph_dict.keys()):
#         return visited_set
#     visited_set.add(current_stop)
#     for i in graph_dict[current_stop]:
#         if i not in visited_set:
#            return dfsHelper(graph_dict,i,visited_set)

# map = [("UPS","Brecon",3),("Jacob City","Owl Ranch",3),("Jacob City","Sunfield",15),("Sunfield","Brecon",25)]
# print(dfs(map, "ups"))


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





#
# map = [("UPS","Brecon",3),("Jacob City","Owl Ranch",3),("Jacob City","Sunfield",15),("Sunfield","Brecon",25)]
# print(dijkstra(map, "ups"))

