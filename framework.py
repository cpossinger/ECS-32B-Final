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
        if self.storage > 20:
            return
        elif pk.address in self.packages:
            self.packages[pk.address].append(pk.id)
            pk.collected = True
            self.storage += 1
        else:
            self.packages[pk.address] = [pk.id]
            pk.collected = True
            self.storage += 1


    def deliverPackage(self, pk):
        if self.storage == 0:
            return
        for pk in self.packages:
            if len(self.packages[pk.address]) == 1:
                pk.delivered = True
                del self.packages[pk.address]
            else:
                pk.delivered = True
                del self.packages[pk.address[pk.id]]


    def deliverPackageByAddress(self, addr):
        pk_w_input_addy = self.packages[addr].values()
        for package in  pk_w_input_addy:
            self.deliverPackage(self,package)
        return

    def removePackage(self, pk, office):
        pk_2_remove = self.packages[pk.address].pop(pk.id)
        self.driveTo(self,self.location,office)
        pk_2_remove.office = office
        pk_2_remove.collected = False
        return

    def driveTo(self, loc1, loc2):
        if loc1 != self.location:
            self.driveTo(self.location, loc1)
        self.location = loc2

    def getPackagesIds(self):
        packID = []
        adds = list(self.packages.values()) #list of dictionaries of id->package
        if adds == []:
            return packID
        for i in range(len(adds)):
            p = list(adds.values()) #list of packages at a given location
            if p == []: #check if address is empty
                continue
            else:
                for k in range(len(p)):
                    packID.append(p[k])
        return packID





