import unittest
from inventory_allocator import InventoryAllocator


class InventoryAllocatorTest(unittest.TestCase):
    def testExact(self):
        order = {"apple": 1}
        stock = [{"name": "owd", "inventory": {"apple": 1}}]
        output = [{"owd": {"apple": 1}}]
        self.assertEqual(output, InventoryAllocator().cheapestShipment(order, stock))
        
    def testNull(self):
        order = {}
        stock = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        output = []
        self.assertEqual(output, InventoryAllocator().cheapestShipment(order, stock))

    def testInsufficient(self):
        order = {"apple": 2}
        stock = [{"name": "owd", "inventory": {"apple": 0}}]
        output = []
        self.assertEqual(output, InventoryAllocator().cheapestShipment(order, stock))

    def testExactMultiple(self):
        order = {"apple": 10}
        stock = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        output = [{"owd": {"apple": 5}}, {"dm": {"apple": 5}}]
        self.assertEqual(output, InventoryAllocator().cheapestShipment(order, stock))

    def testMultipleInsufficient(self):
        order = {"apple": 10, "mango": 20}
        stock = [{"name": "owd", "inventory": {"apple": 9, "mango": 10}}, {"name": "dm", "inventory": {"apple": 0, "mango": 5}}]
        output = []
        self.assertEqual(output, InventoryAllocator().cheapestShipment(order, stock))
        
    def testMultipleOrdersInsufficient(self):
        order = {"apple": 10, "mango": 3, "orange": 100}
        stock = [{"name": "owd", "inventory": {"apple": 1, "mango": 1}}, {"name": "dm", "inventory": {"orange": 25}}]
        output = []
        self.assertEqual(output, InventoryAllocator().cheapestShipment(order, stock))

    def testUnavailable(self):
        order = {"mango": 20}
        stock = [{"name": "owd", "inventory": {"apple": 5}}, {"name": "dm", "inventory": {"apple": 5}}]
        output = []
        self.assertEqual(output, InventoryAllocator().cheapestShipment(order, stock))

    def testSurplus(self):
        order = {"apple": 5}
        stock = [{"name": "owd", "inventory": {"apple": 100}}]
        output = [{"owd": {"apple": 5}}]
        self.assertEqual(output, InventoryAllocator().cheapestShipment(order, stock))



        
if __name__ == "__main__":
    unittest.main()