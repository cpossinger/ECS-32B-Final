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
            #self.driveTo(self.location, loc1)
        self.location = loc2
        return

    def getPackagesIds(self):
        packID = []
        for address in self.packages.values():
            for id in address.keys():
                packID.append(id)
        return packID
        # packID = []
        # adds = list(self.packages.values()) #list of dictionaries of id->package
        # if adds == []:
        #     return packID
        # for i in range(len(adds)):
        #     p = list(adds.values()) #list of packages at a given location
        #     if p == []: #check if address is empty
        #         continue
        #     else:
        #         for k in range(len(p)):
        #             packID.append(p[k])
        # return packID


