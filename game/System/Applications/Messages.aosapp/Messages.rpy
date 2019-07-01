# 
# Messages.rpy
# AliceOS
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init 10 python:
    class ASMessages(ASAppRepresentative):
        bundleName = "Messages"
        bundleId = "app.aliceos.messages"
        bundleDir = AS_DEFAULT_APP_DIR + "Messages/"
        bundleAuthor = "Project Alice"
        bundleVersion = "2.0.0"
        bundleDescription = """\
            Receive and sned messages from your favorite characters.
        """

        requires = {
            AS_REQUIRES_NOTIFICATIONKIT
        }

        def applicationShouldRequestNotification(self):
            return True

        def __init__(self):
            ASAppRepresentative.__init__(self, AS_DEFAULT_APP_DIR + "Messages.aosapp/")

    messages = ASMessages()
