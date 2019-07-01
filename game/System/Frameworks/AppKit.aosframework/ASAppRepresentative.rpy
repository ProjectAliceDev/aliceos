# 
# ASAppRepresentative.rpy
# AliceOS
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

# Set AliceOS permissions if they don't exist yet.
init -1000 python:
    if not persistent.AS_PERMISSIONS:
        persistent.AS_PERMISSIONS = {}

init python:
    
    # Class representation of an app on AliceOS.
    class ASAppRepresentative(object):
        bundleName = "Bundle name"
        bundleId = "app.aliceos.bundle"
        bundleDir = AS_APPS_DIR + "Bundle/"
        bundleAuthor = "Author"
        bundleVersion = "1.0.0"
        bundleDescription = """\
            No description has been provided.
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
        
        # Initialize and create a blank template for permissions.
        def __init__(self, appDirectory):
            if self.bundleId not in persistent.AS_PERMISSIONS:
                persistent.AS_PERMISSIONS[self.bundleId] = {
                    AS_REQUIRES_NOTIFICATIONKIT: False,
                    AS_REQUIRES_FULL_DISK_ACCESS: False,
                    AS_REQUIRES_SYSTEM_EVENTS: False
                }
            else:
                if persistent.AS_PERMISSIONS[self.bundleId][AS_REQUIRES_NOTIFICATIONKIT] == None:
                    persistent.AS_PERMISSIONS[self.bundleId][AS_REQUIRES_NOTIFICATIONKIT] = False

                if persistent.AS_PERMISSIONS[self.bundleId][AS_REQUIRES_FULL_DISK_ACCESS] == None:
                    persistent.AS_PERMISSIONS[self.bundleId][AS_REQUIRES_FULL_DISK_ACCESS] = False

                if persistent.AS_PERMISSIONS[self.bundleId][AS_REQUIRES_SYSTEM_EVENTS] == None:
                    persistent.AS_PERMISSIONS[self.bundleId][AS_REQUIRES_SYSTEM_EVENTS] = False
        
            self.bundleDir = appDirectory
            
            self.icons = {
                16: self.bundleDir + "Resources/Iconset/16.png",
                24: self.bundleDir + "Resources/Iconset/24.png",
                32: self.bundleDir + "Resources/Iconset/32.png",
                64: self.bundleDir + "Resources/Iconset/64.png",
                128: self.bundleDir + "Resources/Iconset/128.png",
                256: self.bundleDir + "Resources/Iconset/256.png"
            }
        
            pass

        # Requests all permissions associated with the app.
        def requestAllPermissions(self):
            store.AS_REQUIRES_NOTIFICATIONKIT = False
            store.AS_REQUIRES_FULL_DISK_ACCESS = False
            store.AS_REQUIRES_SYSTEM_EVENTS = False
        
            if AS_REQUIRES_NOTIFICATIONKIT in self.requires:
                renpy.call_screen("ASPermissionRequest", bundleName=self.bundleName, requestingFor=AS_REQUIRES_NOTIFICATIONKIT, onAcceptRequest=[SetVariable("AS_REQUIRES_NOTIFICATIONKIT", True), Return(0)])
            
            if AS_REQUIRES_FULL_DISK_ACCESS in self.requires:
                renpy.call_screen("ASPermissionRequest", bundleName=self.bundleName, requestingFor=AS_REQUIRES_FULL_DISK_ACCESS, onAcceptRequest=[SetVariable("AS_REQUIRES_FULL_DISK_ACCESS", True), Return(0)])
            
            if AS_REQUIRES_SYSTEM_EVENTS in self.requires:
                renpy.call_screen("ASPermissionRequest", bundleName=self.bundleName, requestingFor=AS_REQUIRES_SYSTEM_EVENTS, onAcceptRequest=[SetVariable("AS_REQUIRES_SYSTEM_EVENTS", True), Return(0)])
            
            persistent.AS_PERMISSIONS[self.bundleId] = {
                AS_REQUIRES_SYSTEM_EVENTS: AS_REQUIRES_SYSTEM_EVENTS,
                AS_REQUIRES_FULL_DISK_ACCESS: AS_REQUIRES_FULL_DISK_ACCESS,
                AS_REQUIRES_NOTIFICATIONKIT: AS_REQUIRES_NOTIFICATIONKIT
            }

        # Steps to take when starting the app.
        def applicationWillLaunch(self):
            return
        
        # Steps to take when the app has finally finished launching.
        def applicationDidLaunch(self):
            return
        
        # Steps to take when the app is about to terminate.
        def applicationWillTerminate(self):
            return
        
        # Steps to take when the app is terminated.
        def applicationDidTerminate(self):
            return
        
        # Determine whether the app can safely send a notification request.
        def applicationShouldRequestNotification(self):
            if persistent.AS_PERMISSIONS[self.bundleId] == None:
                return False
            else:
                return persistent.AS_PERMISSIONS[self.bundleId][AS_REQUIRES_NOTIFICATIONKIT]
            return

        # Steps to take when the app is about to send a notification
        def applicationWillRequestNotification(self, message, withDetails, responseCallback=Return(0)):
            if self.applicationShouldRequestNotification():
                renpy.call_screen("ASNotificationBanner", applet=self, message=message, withDetails=withDetails, responseCallback=responseCallback)
            else:
                print "This app is not authorized to send notifications."
            return
        
        # Steps to take when the app is done sending a notification
        def applicationDidRequestNotification(self):
            return
