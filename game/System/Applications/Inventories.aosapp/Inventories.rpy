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

        def __init__(self):
            ASAppRepresentative.__init__(self, AS_DEFAULT_APP_DIR + "Inventories.aosapp/")

    inventory = ASInventories()