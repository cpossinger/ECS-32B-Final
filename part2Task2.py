"""
Import your Package and Truck classes at the beginning
"""
from csv import *
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




class Package:
    def __init__(self, id,address = "",office = "",ownerName = ""):
        self.id = id
        self.address = address
        self.office = office
        self.ownerName = ownerName
        self.collected = False
        self.delivered = False



class Truck:
    def __init__(self, id, n, loc):
        self.id = id
        self.size = n
        self.location = loc
        self.packages = dict()
        self.storage = len(self.packages)

    def collectPackage(self, pk):
        if self.location == pk.office:
            if self.storage >= self.size:
                return
            elif pk.address in self.packages.keys():
                self.packages[pk.address][pk.id] = pk
                self.packages[pk.address][pk.id].collected = True
                self.storage += 1
            else:
                self.packages[pk.address] = {pk.id: pk}
                self.packages[pk.address][pk.id].collected = True
                self.storage += 1
        else:
            return

    def deliverPackage(self, pk):
        if self.location == pk.address:
            if self.storage == 0:
                return
            self.driveTo(self.location, pk.address)
            pk_2_deliver = self.packages[pk.address].pop(pk.id)
            self.storage -= 1
            pk_2_deliver.delivered = True
            return
        else:
            return


    def deliverPackageByAddress(self, addr):
        pk_ids_output = []
        if self.location == addr:
            pk_w_input_addy = self.packages[addr].keys()
            for id in list(pk_w_input_addy):
                pk_2_deliver = self.packages[addr].pop(id)
                self.storage -= 1
                pk_2_deliver.delivered = True
                pk_ids_output.append(pk_2_deliver)
            return pk_ids_output
        else:
            return

    def removePackage(self, pk, office):
        if self.location == office and pk.collected == True:
            pk_2_remove = self.packages[pk.address].pop(pk.id)
            self.storage -= 1
            pk_2_remove.office = office
            pk_2_remove.collected = False
            return
        else:
            return

    def driveTo(self, loc1, loc2):
        if loc1 != self.location:
            return
        self.location = loc2
        return

    def getPackagesIds(self):
        packID = []
        for address in self.packages.values():
            for id in address.keys():
                packID.append(id)
        return packID




"""
deliveryService
"""
def deliveryService(map, truck, packages):
    packages = set(packages)
    deliveredTo = {}
    stops = []
    while True:
        # collect packages from post office
        truck_empty = False
        for pk in packages:
            truck.collectPackage(pk)


        # initialize new addresses from collected packages
        addresses = []
        # extract the addresses of the packages on board truck

        for pk in truck.packages:
            if truck.packages[pk]:
                addresses.append(pk)
        if addresses != []:

            while truck_empty == False:
                address_dist = []
                # get shortest paths of all stops
                gps_dict,distance = dijkstra(map,truck.location)
                # extract the addresses distances of the packages on board truck
                for addy in addresses:
                    address_dist.append(distance[addy])
                # choose shortest distance for next stop
                next_stop_val = min(address_dist)
                next_stop_val_index = address_dist.index(next_stop_val)
                next_stop = addresses[next_stop_val_index]
                # drive to next stop
                for stop in gps_dict[next_stop][1:]:
                    truck.driveTo(truck.location,stop)
                    stops.append(stop)
                # deliver packages
                pk_delivered = truck.deliverPackageByAddress(truck.location)
                for pk in pk_delivered:
                    deliveredTo[pk.id] = truck.location
                    packages.remove(pk)
                # remove addresses already visited
                addresses.pop(addresses.index(next_stop))
                address_dist.pop(next_stop_val_index)


                # all packages in the truck are delivered

                if addresses == []:
                    truck.packages.clear()
                    truck_empty = True
        else:
            # if total packages are all delivered exit outer while loop
            if len(packages) == 0:
                break

            gps_dict,distance = dijkstra(map,truck.location)
            #    find nearest post office
            for key, value in list(distance.items()):
                if "UPS" not in key:
                    del distance[key]
            while True:
                next_stop_dist = min(list(distance.values()))
                for key,value in distance.items():
                    if value == next_stop_dist:
                        next_stop = key
                for i in packages:
                    if i.office == next_stop:
                        packages_at_next_stop = True
                if packages_at_next_stop == True:
                    packages_at_next_stop = False
                    break
                else:
                    del distance[next_stop]

            for stop in gps_dict[next_stop][1:]:
                truck.driveTo(truck.location, stop)
                stops.append(stop)



    return (deliveredTo, stops)

































