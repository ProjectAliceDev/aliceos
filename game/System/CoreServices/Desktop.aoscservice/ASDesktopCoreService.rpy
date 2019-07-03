# 
# ASDesktopCoreService.rpy
# AliceOS
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init 5 python:

    class ASDesktopCoreService(ASCoreServiceRepresentative):
        bundleName = "Desktop"
        bundleId = "app.aliceos.core-services.desktop"
        bundleDir = AS_CORESERVICES_DIR + "Desktop.aoscservice/"
        bundleAuthor = "Project Alice"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            Desktop provides quick access to applications in AliceOS.
        """

        # The desktop is a core service, but it doesn't require any explicit permissions.
        requires = { }

        # Looks for all apps using AppKit and returns a list of them.
        def gatherAllApplications(self):
            import gc
            apps = []
            for obj in gc.get_objects():
                if isinstance(obj, ASAppRepresentative):
                    apps.append(obj)
            return apps

        def gatherCurrentTime(self):
            from time import gmtime, strftime
            return strftime("%a. %I:%M %p")

        def showDesktop(self):
            renpy.call_screen("ASDesktopShellView")

        def showTopBar(self):
            renpy.call_screen("ASDesktopTopBar")

        def __init__(self):
            ASCoreServiceRepresentative.__init__(self, AS_CORESERVICES_DIR + "Desktop.aoscservice/")

    ASDesktop = ASDesktopCoreService()
