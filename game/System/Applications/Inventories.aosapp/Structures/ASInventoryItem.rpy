# 
# ASInventoryItem.rpy
# AliceOS
# 
# Created by Marquis Kurt on 9/13/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

init 10 python:
    class ASInventoryItem(object):

        def __init__(self, itemId=None, name="Item", description="", canBeUsed=True, specialUseCase=None, canBeUsedOnce=False, imageName=ASInventories.bundleDir + "Resources/Item.png"):
            self.name = name
            self.description = description
            self.canBeUsed = canBeUsed
            self.canBeUsedOnce = canBeUsedOnce
            self.runSpecialUseCase = specialUseCase if callable(specialUseCase) else None
            self.imageName = imageName
            self.itemId = itemId

        def __repr__(self):
            return '<ASInventoryItem "%s" "%s">' % (str(self.itemId), str(self.name))

        def __eq__(self, other):
            if not isinstance(other, ASInventoryItem):
                return False
            if self.itemId is None and other.itemId is None:
                return self.name == other.name
            else:
                return self.itemId == other.itemId

        def useItem(self):
            if self.canBeUsed:
                if self.runSpecialUseCase is not None:
                    self.runSpecialUseCase()
                if self.canBeUsedOnce:
                    self.canBeUsed = False
                    return True

            else:
                print("WARN: This item cannot be used.")
                return False
