from collections import defaultdict
import sys
from heapq import *



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
        visited_dict[current_stop] = "Visited"
        path_dict[current_stop] = getPath(office,current_stop,[],pred_dict)
        graph_dict[current_stop].sort()
        for i in graph_dict[current_stop]:
            if visited_dict[i] == "Unvisited":
                queue.append(i)
                pred_dict[i] = current_stop
                visited_dict[i] = "Visiting"
    for i in path_dict.keys():
        path_dict[i].reverse()

    return path_dict


def getPath(office,current_pred,path,pred_dict):
    if current_pred == office:
        return path + [office]
    path.append(current_pred)
    return getPath(office,pred_dict[current_pred],path,pred_dict)



"""
DFS
"""



def dfs(map, office):
    graph_dict = defaultdict(list)
    visited_dict = {}
    path_dict = defaultdict(list)
    pred_dict = {}

    for u, v, w in map:
        graph_dict[u].append(v)
        graph_dict[v].append(u)
        visited_dict[u] = "Unvisited"
        visited_dict[v] = "Unvisited"
    stack = []
    stack.append(office)
    visited_dict[office] = "Visited"
    pred_dict[office] = []
    while stack:
        current_stop = stack.pop()
        visited_dict[current_stop] = "Visiting"
        path_dict[current_stop] = getPath(office, current_stop, [], pred_dict)
        graph_dict[current_stop].sort()
        for i in graph_dict[current_stop]:
            if visited_dict[i] == "Unvisited":
                stack.append(i)
                pred_dict[i] = current_stop
        visited_dict[i] = "Visited"
    for i in path_dict.keys():
        path_dict[i].reverse()

    return path_dict


def getPath(office,current_pred,path,pred_dict):
    if current_pred == office:
        return path + [office]
    path.append(current_pred)
    return getPath(office,pred_dict[current_pred],path,pred_dict)

"""
Dijkstra's
"""

# def dijkstra(map,office):
#     graph_dict = defaultdict(list)
#     path_dict = defaultdict(list)
#     for u,v,w in map:
#         graph_dict[u].append((w,v))
#         graph_dict[v].append((w,u))
#     print(graph_dict)
#     for i in graph_dict.keys():
#         path_dict[i] = dijkstraHelper(graph_dict,office,i)[1]
#     return path_dict
#



# def dijkstraHelper(graph_dict,office,destination):
#     minHeap = []
#     vertices_seen = set()
#     minHeap = [(0,office,())]
#     mins = {office:0}
#
#     while minHeap:
#         print(minHeap)
#         (cost,vertex1,path) = heappop(minHeap)
#         if vertex1 not in vertices_seen:
#             vertices_seen.add(vertex1)
#             path = (vertex1,path)
#             if vertex1 == destination:
#                 return (cost,path)
#             for cost_iter,vertex2 in graph_dict.get(vertex1,()):
#                 if vertex2 in vertices_seen:
#                     continue
#                 previous = mins.get(vertex2,None)
#                 next = cost + cost_iter
#                 if previous is None or next < previous:
#                     mins[vertex2] = next
#                     heappush(minHeap,(next,vertex2,path))
#     return sys.maxsize,None

# def dijkstra(map,office):
#     graph_dict = defaultdict(list)
#     dist_dict = {}
#     for u, v, w in map:
#         graph_dict[u].append(v)
#         graph_dict[v].append(u)
#         dist_dict[u,v] = w
#         dist_dict[v,u] = w
#
#     visit_dict = {office:0}
#     heap = [(0,office)]
#     path = {}
#
#     vertices = set(graph_dict.keys())
#
#     while vertices and heap:
#         cur_weight,min_vertex = heappop(heap)
#         try:
#             while min_vertex not in vertices:
#                 cur_weight,min_vertex = heappop(heap)
#         except IndexError:
#             break
#         vertices.remove(min_vertex)
#
#         for vertex in graph_dict[min_vertex]:
#             weight = cur_weight + dist_dict[min_vertex,vertex]
#             if vertex not in visit_dict or weight < visit_dict[vertex]:
#                 heappush(heap,(weight,vertex))
#                 path[vertex] = min_vertex
#     visit_dict[office] = [office]
#     return visit_dict,path
#

#
# def dijkstra(map,office):
#     dist_dict = {}
#     graph_dict = defaultdict(list)
#     pred_dict = defaultdict(list)
#     heap = []
#
#     dist_dict[office] = 0
#     for u,v,w in map:
#         graph_dict[u].append((v,w))
#         graph_dict[v].append((u,w))
#
#     for i in list(graph_dict.keys())[1:]:
#         dist_dict[i] = sys.maxsize
#     for i in graph_dict.keys():
#         pred_dict[i].append(None)
#         heappush(heap,(dist_dict[i],i))
#     while heap:
#         u = nsmallest(heap)
#         for v in graph_dict[u]:
#             if dist_dict[v] > dist_dict[u] + w[v,u] and v in heap:
#                 dist_dict[v] = dist_dict[u] + w[v,u]
#
#
#
#
#     return None
#
#
# map = [("UPS","Brecon",3),("Jacob City","Owl Ranch",3),("Jacob City","Sunfield",15),("Sunfield","Brecon",25)]
# print(dijkstra(map, "UPS"))
#
