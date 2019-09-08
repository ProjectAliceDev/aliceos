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

        # Looks for all apps using AppKit and returns a list of them.
        def gatherAllApplications(self):
            import gc
            apps = []
            for obj in gc.get_objects():
                if isinstance(obj, ASAppRepresentative):
                    apps.append(obj)
            return apps
        
        def boot(self, timeout=5, expressSetup=True, disclaimer=None, bootView="ASBootloaderView"):
            if not persistent.AS_COMPLETED_SETUP:
                ASSetup.startSetup(express=expressSetup, disclaimer=disclaimer)

            for app in self.gatherAllApplications():
                if app.applicationWillLaunchAtLogin is not None and app.applicationShouldLaunchAtLogin():
                    app.applicationWillLaunchAtLogin()
                else:
                    if AS_REQUIRES_SYSTEM_EVENTS in app.requires and not app.applicationShouldLaunchAtLogin():
                        print("WARN: %s cannot run its login service because it doesn't have permission to do so." % (app.bundleName,))
                    else:
                        print("INFO: Skipping %s (%s) login service because it doesn't have one." % (app.bundleName, app.bundleId, ) )

            renpy.call_screen(bootView, timeout=timeout)
    
        def __init__(self):
            ASCoreServiceRepresentative.__init__(self, AS_CORESERVICES_DIR + "Boot.aoscservice/")
    
    ASBootloader = ASBootloaderCoreService()
