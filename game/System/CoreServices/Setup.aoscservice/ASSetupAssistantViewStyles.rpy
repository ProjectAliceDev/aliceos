# 
# ASSetupAssistantViewStyles.rpy
# AliceOS
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init:
    style ASSetupAssistantViewFrame:
        background Frame([ASSetup.getFromElements("Window.png")], gui.confirm_frame_borders, tile=gui.frame_tile)
        xalign 0.5
        yalign 0.5

    style ASSetupAssistantViewTitle is ASSystemBoldFont:
        size 28
        color "#ffffff"

    style ASSetupAssistantViewDetail is ASSystemRegularFont:
        size 18
        color "#ffffff"

    style ASSetupAssistantViewSmallerDetail is ASSystemMediumFont:
        size 10
        color "#999999"

    style ASSetupAssistantViewButton is gui_button:
        background Frame([ASSetup.getFromElements("Button.png")], gui.confirm_frame_borders, tile=gui.frame_tile)
        hover_background Frame([ASSetup.getFromElements("ButtonHover.png")], gui.confirm_frame_borders, tile=gui.frame_tile)

    style ASSetupAssistantViewButton_text is ASSystemMediumFont:
        size 20
        color "#000000"

    style ASSetupAssistantViewInput is ASSystemRegularFont:
        size 20
        color "#ffffff"
