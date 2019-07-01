# 
# ASAppRepresentative.rpy
# AliceOS
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init -1000 python:
    if not persistent.AS_PERMISSIONS:
        persistent.AS_PERMISSIONS = {}
init python:
    class ASAppRepresentative(object):
        bundleName = "Bundle name"
        bundleId = "app.aliceos.bundle"
        bundleDir = AS_APPS_DIR + "Bundle"
        bundleAuthor = "Author"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            This is a bundle description.
        """

        icons = {
            16: bundleDir + "Resources/Iconset/16.png",
            24: bundleDir + "Resources/Iconset/24.png",
            32: bundleDir + "Resources/Iconset/32.png",
            64: bundleDir + "Resources/Iconset/64.png",
            128: bundleDir + "Resources/Iconset/128.png",
            256: bundleDir + "Resources/Iconset/256.png"
        }

        requires = {
            AS_REQUIRES_NOTIFICATIONKIT,
            AS_REQUIRES_FULL_DISK_ACCESS,
            AS_REQUIRES_SYSTEM_EVENTS
        }

        # Requests all necessary permissions for this app.
        def requestAllPermissions(self):
            store.AS_REQUIRES_NOTIFICATIONKIT = False
            store.AS_REQUIRES_FULL_DISK_ACCESS = False
            store.AS_REQUIRES_SYSTEM_EVENTS = False

        def applicationWillLaunch(self):
            return

        def applicationDidLaunch(self):
            return

        def applicationWillTerminate(self):
            return

        def applicationDidTerminate(self):
            return

        def applicationWillRequestNotification(self):
            return

        def applicationDidRequestNotification(self):
            return
