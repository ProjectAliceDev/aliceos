# 
# ASDesktopTopBar.rpy
# AliceOS
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init screen ASDesktopTopBar:
    tag ASDesktopTopBar
    zorder 500
    modal False

    add ASDesktop.bundleDir + "Resources/Elements/TopBar.png"

    vbox:
        xfill True
        ysize 48
        
        hbox:
            xfill True
            yfill True

            textbutton _("Activities"):
                style "ASDesktopTopBarButton"
                xalign 0.025
                yalign 0.5
            
            $ store.currentDesktopTime = ASDesktop.gatherCurrentTime()
            
            text store.currentDesktopTime:
                style "ASDesktopTopBarStaticText"
                xalign 0.955
                yalign 0.4

        timer 1 action SetVariable("store.currentDesktopTime", ASDesktop.gatherCurrentTime()) repeat True
