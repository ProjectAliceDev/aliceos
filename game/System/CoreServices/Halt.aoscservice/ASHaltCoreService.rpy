# 
# ASHaltCoreService.rpy
# AliceOS
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init 5 python:

    class ASHaltCoreService(ASCoreServiceRepresentative):
        bundleName = "Error Halt System"
        bundleId = "app.aliceos.core-services.halt"
        bundleDir = AS_CORESERVICES_DIR + "Halt.aoscservice/"
        bundleAuthor = "Project Alice"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            Safely catch system-level errors and restart AliceOS.
        """

        def halt(self, code=""):
            renpy.call_screen("ASHaltMessage", error=code)
            renpy.utter_restart()

        def __init__(self):
            ASCoreServiceRepresentative.__init__(self, AS_CORESERVICES_DIR + "Halt.aoscservice/")

    ASHalt = ASHaltCoreService()
