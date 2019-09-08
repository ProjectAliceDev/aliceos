#
# ASWindowTitleBar.rpy
# AliceOS
#
# Created by Marquis Kurt on 9/8/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

screen ASWindowTitleBar(name="ASWindow"):
    hbox:
        style_prefix "ASWindowTitleBar"
        xfill True

        text name

        imagebutton auto AS_FRAMEWORK_DIR("ScreenKit") + "Resources/wcClose_%s.png" action Return("didCloseView"):
            xalign 1.0

style ASWindowTitleBar_hbox is hbox:
    xalign 0.0
    yalign 0.5
    spacing 8

style ASWindowTitleBar_text:
    font AS_FONTS_DIR + "Medium.ttf"
    size 16
    xalign 0.0