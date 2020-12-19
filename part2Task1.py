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

def dijkstra(map,office):
    graph_dict = defaultdict(list)
    path_dict = defaultdict(list)
    pred_dict = {}
    distance = {}
    minHeap = []

    for u, v, w in map:
        graph_dict[u].append((v,w))
        graph_dict[v].append((u,w))

    for vertex in graph_dict.keys():
        distance[vertex] = sys.maxsize
        heappush(minHeap,(distance[vertex],vertex))

    office_index = [y[1] for y in minHeap].index(office)
    minHeap[office_index] = (0,office)
    distance[office] = 0
    pred_dict[office] = office
    while minHeap:
        heapify(minHeap)
        smallest_heap_val = heappop(minHeap)
        u = smallest_heap_val[1]

        for adj in graph_dict[u]:
                v = adj[0]
                if v in [y[1] for y in minHeap] and distance[u] != sys.maxsize and adj[1] + distance[u] < distance[v]:
                    v_index = [y[1] for y in minHeap].index(v)
                    distance[v] = adj[1] + distance[u]
                    pred_dict[v] = u
                    minHeap[v_index] = (distance[v],v)
        path_dict[u] = getPath(office, u, [], pred_dict)

    for i in path_dict.keys():
        path_dict[i].reverse()
    return path_dict,distance

def getPath(office,current_pred,path,pred_dict):
    if current_pred == office:
        return path + [office]
    path.append(current_pred)
    return getPath(office,pred_dict[current_pred],path,pred_dict)

