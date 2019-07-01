# 
# ASNotificationBanner.rpy
# AliceOS
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init screen ASNotificationBanner(applet=None, message, withDetails, responseCallback=Return('didClickRespond')):
    tag ASNotificationBanner
    zorder 100
    style_prefix "ASNotificationBanner"
    
    frame at ASNotificationBannerTransition:
        style "ASNotificationBannerFrame"
        xpadding 24
        ypadding 24
        xalign 0.5
        yalign 0.025
        xsize 676
    
        vbox:
            hbox:
                textbutton _("Respond") action responseCallback:
                    style "ASNotificationBannerButton"
                    xalign 1.0
                    ypadding 0
            null height 8
            text message:
                style "ASNotificationBannerTitle"
            text withDetails:
                style "ASNotificationBannerDetail"
