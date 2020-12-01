class Package:
    def __init__(self, id):
        self.id = id
        self.address = ""
        self.office = ""
        self.ownerName = ""
        self.collected = False
        self.delivered = False



class Truck:
    def __init__(self, id, n, loc):
        self.id = id
        self.size = n
        self.location = loc
        # self.packages = ?


    def collectPackage(self, pk):


    def deliverPackage(self, pk):


    def deliverPackageByAddress(self, addr):
        

    def removePackage(self, pk, office):


    def driveTo(self, loc1, loc2):


    def getPackagesIds(self):





