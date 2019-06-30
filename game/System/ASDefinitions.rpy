# 
# ASDefinitions.rpy
# AliceOS
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

# MARK: OS directory definitions
# Define system-wide directories here. These definitions are used
# to prevent re-typing common directory locations.
define AS_SYSTEM_DIR = "System/"
define AS_FRAMEWORKS_DIR = "System/Frameworks/"
define AS_CORESERVICES_DIR = "System/CoreServices/"
define AS_DEFAULT_APP_DIR = "System/Applications/"
define AS_FONTS_DIR = "System/Fonts/"
define AS_APPS_DIR = "Applications/"

init python:
    
    # Get the framework directory from the framework name. This function
    # is intended to prevent re-typing of framework locations for typical
    # AliceOS frameworks.
    def AS_FRAMEWORK_DIR(FRAMEWORK_NAME="Default"):
        return AS_FRAMEWORKS_DIR + "/" + FRAMEWORK_NAME + ".aosframework/"

# MARK: OS permissions definitions
define AS_REQUIRES_NOTIIFICATIONKIT = "REQ_NOTIFICATIONKIT"
define AS_REQUIRES_FULL_DISK_ACCESS = "REQ_FULL_DISK"
define AS_REQUIRES_SYSTEM_EVENTS = "REQ_SYSTEM_EVENTS"
