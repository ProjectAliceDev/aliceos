# 
# ASSetupAssistantView.rpy
# AliceOS
#
# Created by Marquis Kurt on 7/4/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

# MARK: ASSetupAssistantView screen entry point
init screen ASSetupAssistantView(title="Setup Assistant", instructions="", useInputMethod=False, completed=False):
    tag ASSetupAssistantView
    zorder 100
    modal True

    add ASSetup.getFromElements("Background.png")

    frame:
        style "ASSetupAssistantViewFrame"
        xalign 0.5
        yalign 0.5
        ysize 650
        xsize 850
        padding (64, 48)


        has vbox:
            xalign 0.5
            xfill True
            yfill True
            
            hbox:
                xalign 0.5
                spacing 8
                add ASSetup.icons[32]
                text title:
                    style "ASSetupAssistantViewTitle"
                    xalign 0.5

            text instructions:
                style "ASSetupAssistantViewDetail"
                xalign 0.5
            
            if useInputMethod:
                input:
                    style "ASSetupAssistantViewInput"
                    xalign 0.5
            else:
                button action Return('didCompleteStep'):
                    style "ASSetupAssistantViewButton"
                    xalign 0.5
                    yalign 0.85
                    xpadding 128
                    
                    if completed:
                        text "Finish":
                            style "ASSetupAssistantViewButton_text"
                    else:
                        text "Next":
                            style "ASSetupAssistantViewButton_text"
            
            if useInputMethod:
                null height 16
                text "To continue, press Return or Enter.":
                    style "ASSetupAssistantViewSmallerDetail"
                    xalign 0.5
                    yalign 0.75
