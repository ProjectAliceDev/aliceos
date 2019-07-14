# 
# ASBootloaderCoreService.rpy
# AliceOS
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init 5 python:
    
    class ASBootloaderCoreService(ASCoreServiceRepresentative):
        bundleName = "Bootloader"
        bundleId = "app.aliceos.core-services.boot"
        bundleDir = AS_CORESERVICES_DIR + "Boot.aoscservice/"
        bundleAuthor = "Project Alice"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            Show a loading screen for AliceOS.
        """
        
        def boot(self, timeout=5, expressSetup=True, disclaimer=None):
            renpy.call_screen("ASBootloaderView", timeout=timeout)
            if not persistent.AS_COMPLETED_SETUP:
                ASSetup.startSetup(express=expressSetup, disclaimer=disclaimer)
    
        def __init__(self):
            ASCoreServiceRepresentative.__init__(self, AS_CORESERVICES_DIR + "Boot.aoscservice/")
    
    ASBootloader = ASBootloaderCoreService()
