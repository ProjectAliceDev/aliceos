#
# ScreenStyles.rpy
# AliceOS
#
# Created by Marquis Kurt on 9/8/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init offset = 10

style ASWindowFrame:
    background Frame([AS_FRAMEWORK_DIR("ScreenKit") + "Resources/FrameChrome.png"], Borders(8,12,8,8), tile=False)
    padding (16, 16)
    xalign 0.5
    yalign 0.5


style ASVerticalBox is vbox:
    spacing 8

style ASVerticalBox_text:
    font AS_FONTS_DIR + "Regular.ttf"

style ASVerticalBox_button is gui_button
style ASVerticalBox_button_text:
    font AS_FONTS_DIR + "Bold.ttf"