def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)

def displayInventory(inventory):
    print("Inventory:")
    total_items = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total_items += v
    print("Total number of items: " + str(total_items))

displayInventory(inv)
