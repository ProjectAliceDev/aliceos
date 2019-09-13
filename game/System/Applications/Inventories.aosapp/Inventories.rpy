# 
# Inventories.rpy
# AliceOS
# 
# Created by Marquis Kurt on 9/13/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

init 10 python:

    class ASInventories(ASAppRepresentative):
        bundleName = "Inventories"
        bundleId = "app.aliceos.inventories"
        bundleDir = AS_DEFAULT_APP_DIR + "Inventories.aosapp/"
        bundleAuthor = "Project Alice"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            View, use, and manage items you receive in-game with Inventories, a simple app designed for make item inventory systems easy.
        """

        requires = { AS_REQUIRES_NOTIFICATIONKIT }

        inventory = []

        def applicationWillLaunch(self):
            renpy.show_screen("ASInventoryManagerView")
            return

        def isEmpty(self):
            return len(self.inventory) == 0

        def retrieve(self):
            return self.inventory

        def containsItem(self, item):
            return item in self.inventory

        def lookupItemByName(self, name):
            for item in self.inventory:
                if item.name == name:
                    return item
            return None

        def addItem(self, item):
            if isinstance(item, ASInventoryItem):
                self.inventory.append(item)
                shouldDisplayItem = self.applicationWillRequestNotification("%s received!" % (item.name), "Go to Inventories to learn more.")

                if shouldDisplayItem == "didClickRespond":
                    renpy.show_screen("ASInventoryManagerView", currentItem=item)
            else:
                raise TypeError("Expected item to be ASInventoryItem, but received %s" % (type(item)))

        def useItem(self, item):
            if item in self.inventory:
                shouldDispose = item.useItem()

                if shouldDispose:
                    self.inventory.remove(item)
            else:
                raise KeyError("Item not found in the inventory: %s" % (item,) )

        def importFromList(self, list):

            listAsInventoryChecks = map(lambda x: isinstance(x, ASInventoryItem), list)
            isInventoryReal = reduce(lambda x, y: x and y, listAsInventoryChecks)

            if isInventoryReal:
                self.inventory = list
            else:
                raise TypeError("List contains non-ASInventoryItem items.")


        def __init__(self):
            ASAppRepresentative.__init__(self, AS_DEFAULT_APP_DIR + "Inventories.aosapp/")

    inventory = ASInventories()