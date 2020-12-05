import unittest
from gradescope_utils.autograder_utils.decorators import weight, visibility
from project import *


def updatePackage(pk, addr, off, name):
    pk.address = addr
    pk.office = off
    pk.ownerName = name



# set up the packages and the truck
def setup():
    pk1 = Package("pk1")
    updatePackage(pk1, "addr1", "ups1", "name1")

    pk2 = Package("pk2")
    updatePackage(pk2, "addr2", "ups1", "name2")

    pk3 = Package("pk3")
    updatePackage(pk3, "addr1", "ups2", "name3")

    pk4 = Package("pk4")
    updatePackage(pk4, "addr2", "ups2", "name4")

    pk5 = Package("pk5")
    updatePackage(pk5, "addr2", "ups1", "name5")

    pk6 = Package("pk6")
    updatePackage(pk6, "addr1", "ups2", "name6")

    pk7 = Package("pk7")
    updatePackage(pk7, "addr1", "ups2", "name7")

    pk8 = Package("pk8")
    updatePackage(pk8, "addr2", "ups1", "name8")

    packages = [pk1, pk2, pk3, pk4, pk5, pk6, pk7, pk8]

    # initialize the truck
    truck = Truck("truck", 3, "ups2")
    return (packages, truck)


class TestStop3(unittest.TestCase):
    @weight(3)
    def test1(self):
        """Stop 3 test 1 (3 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        pk7 = packages[6]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.collectPackage(pk7)

        val = sorted(truck.getPackagesIds())
        expected = ["pk3", "pk4", "pk6"]
        self.assertEqual(val, expected)
        

    @weight(2)
    def test2(self):
        """Stop 3 test 2 (2 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        pk7 = packages[6]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.collectPackage(pk7)
        val2 = pk7.collected
        expected2 = False
        self.assertEqual(val2, expected2)
        

    @weight(1)
    def test3(self):
        """Stop 3 test 3 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        pk7 = packages[6]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.collectPackage(pk7)
        val3 = pk7.delivered
        expected3 = False
        self.assertEqual(val3, expected3)
        

    @weight(1)
    def test4(self):
        """Stop 3 test 4 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        pk7 = packages[6]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.collectPackage(pk7)
        val4 = pk7.address
        expected4 = "addr1"
        self.assertEqual(val4, expected4)
        

    @weight(1)
    def test5(self):
        """Stop 3 test 5 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        pk7 = packages[6]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.collectPackage(pk7)
        val5 = pk7.office
        expected5 = "ups2"
        self.assertEqual(val5, expected5)
        

    @weight(1)
    def test6(self):
        """Stop 3 test 6 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        pk7 = packages[6]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.collectPackage(pk7)
        val6 = pk7.ownerName
        expected6 = "name7"
        self.assertEqual(val6, expected6)
        
    @weight(2)
    def test7(self):
        """Stop 3 test 7 (2 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val = truck.getPackagesIds()
        expected = ["pk4"]
        self.assertEqual(val, expected)
        

    @weight(1)
    def test8(self):
        """Stop 3 test 8 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val2 = pk3.collected
        expected2 = True
        self.assertEqual(val2, expected2)
        

    @weight(1)
    def test9(self):
        """Stop 3 test 9 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val3 = pk3.delivered
        expected3 = True
        self.assertEqual(val3, expected3)
        

    @weight(1)
    def test10(self):
        """Stop 3 test 10 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val4 = pk3.address
        expected4 = "addr1"
        self.assertEqual(val4, expected4)
        

    @weight(1)
    def test11(self):
        """Stop 3 test 11 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val5 = pk3.office
        expected5 = "ups2"
        self.assertEqual(val5, expected5)
        

    @weight(1)
    def test12(self):
        """Stop 3 test 12 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val6 = pk3.ownerName
        expected6 = "name3"
        self.assertEqual(val6, expected6)
        


    @weight(1)
    def test13(self):
        """Stop 3 test 13 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val2 = pk4.collected
        expected2 = True
        self.assertEqual(val2, expected2)
        

    @weight(1)
    def test14(self):
        """Stop 3 test 14 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val3 = pk4.delivered
        expected3 = False
        self.assertEqual(val3, expected3)
        

    @weight(1)
    def test15(self):
        """Stop 3 test 15 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val4 = pk4.address
        expected4 = "addr2"
        self.assertEqual(val4, expected4)
        

    @weight(1)
    def test16(self):
        """Stop 3 test 16 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val5 = pk4.office
        expected5 = "ups2"
        self.assertEqual(val5, expected5)
        

    @weight(1)
    def test17(self):
        """Stop 3 test 17 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val6 = pk4.ownerName
        expected6 = "name4"
        self.assertEqual(val6, expected6)
        

    @weight(1)
    def test18(self):
        """Stop 3 test 18 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val2 = pk6.collected
        expected2 = True
        self.assertEqual(val2, expected2)
        

    @weight(1)
    def test19(self):
        """Stop 3 test 19 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val3 = pk6.delivered
        expected3 = True
        self.assertEqual(val3, expected3)
        

    @weight(1)
    def test20(self):
        """Stop 3 test 20 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val4 = pk6.address
        expected4 = "addr1"
        self.assertEqual(val4, expected4)
        

    @weight(1)
    def test21(self):
        """Stop 3 test 21 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val5 = pk6.office
        expected5 = "ups2"
        self.assertEqual(val5, expected5)
        

    @weight(1)
    def test22(self):
        """Stop 3 test 22 (1 point)"""
        packages, truck = setup()
        pk3 = packages[2]
        pk4 = packages[3]
        pk6 = packages[5]
        truck.collectPackage(pk3)
        truck.collectPackage(pk4)
        truck.collectPackage(pk6)
        truck.driveTo("ups2", "addr1")
        truck.deliverPackageByAddress("addr1")
        val6 = pk6.ownerName
        expected6 = "name6"
        self.assertEqual(val6, expected6)
        
