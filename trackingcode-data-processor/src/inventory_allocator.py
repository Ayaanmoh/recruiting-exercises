class InventoryAllocator():
    def cheapestShipment(self, order, stock):
        """
        Parameters:-
        order: Requested items from warehouse
        stock: Current items available in warehouse
        """
        shipment = []
        if len(order) == 0 or len(stock)== 0:
            return []
        #keep track of items left as we move through warehouses
        count = 0
        for item in order:
            count += order[item]
        for warehouse in stock:
            if count == 0:
                break
            name = warehouse["name"]
            inventory = warehouse["inventory"]
            for item in order:
                if order[item] == 0:
                    continue
                #check for item and add to shipment if not present
                if item in inventory and inventory[item] > 0:
                    if shipment == [] or name not in shipment[-1]:
                        shipment.append({name: {}})
                    #check for item count in inventory with order
                    if inventory[item] >= order[item]:
                        count -= order[item]
                        shipment[-1][name][item] = order[item]
                        order[item] = 0
                    else:
                        count -= inventory[item]
                        shipment[-1][name][item] = inventory[item]
                        order[item] -= inventory[item]
        if count > 0:
            return []
        return shipment
