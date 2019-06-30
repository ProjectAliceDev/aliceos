# 
# ASNotificationStyles.rpy
# AliceOS
#
# Created by Marquis Kurt on 6/30/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

# MARK: ASNotificationBanner
init:
    style ASNotificationBannerFrame:
        background Frame([AS_FRAMEWORK_DIR("NotificationKit") + "Resources/bannerBackground.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
            xalign .5
            yalign .5

    transform ASNotificationBannerTransition:
        on show:
            yalign 0.0 xalign 0.5
            linear 0.25 ypos 0.025
        on hide:
            yalign 0.025 xalign 0.5
            linear 0.25 yalign -1.0

    style ASNotificationBannerTitle is ASSystemBoldFont:
        size 24
        color "#000"

    style ASNotificationBannerDetail is ASSystemRegularFont:
        size 20
        color "#000"

    style ASNotificationBannerButton is gui_button
        
    style ASNotificationBannerButton_text is ASSystemBoldFont:
        size 16
        color "#000"
