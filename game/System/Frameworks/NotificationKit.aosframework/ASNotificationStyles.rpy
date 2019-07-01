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

    style ASNotificationBannerSource is ASSystemMediumFont:
        size 20
        color "#f4f4f4"
        first_indent 10
        text_align 0
        layout "tex"
        xalign 0

    style ASNotificationBannerTitle is ASSystemBoldFont:
        size 24
        color "#f4f4f4"

    style ASNotificationBannerDetail is ASSystemRegularFont:
        size 20
        color "#f4f4f4"

    style ASNotificationBannerButton is gui_button
        
    style ASNotificationBannerButton_text is ASSystemBoldFont:
        size 16
        color "#f4f4f4"
