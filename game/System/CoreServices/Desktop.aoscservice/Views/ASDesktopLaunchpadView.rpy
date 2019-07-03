# 
# ASDesktopLaunchpadView.rpy
# AliceOS
#
# Created by Marquis Kurt on 7/3/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
# 

init screen ASDesktopLaunchpadView:
    tag ASDesktopLaunchpadView
    modal False
    
    add ASDesktop.bundleDir + "Resources/Elements/LaunchpadBlur.png"
    
    use ASDesktopTopBar

    vbox:
        yalign 0.45
        xalign 0.5

        $ apps = ASDesktop.gatherAllApplications()

        if apps == []:
            text _("No apps installed."):
                style "ASDesktopLaunchpadViewCenteredText"
        else:
            grid len(apps) 1:
                for i in range(len(apps) * 1):
                    $ slot = i + 1
                    button:
                        maximum (128, 144)
                        action [apps[i].applicationWillLaunch(), Hide("ASDesktopLaunchpadView")]
                        has vbox:
                            xalign 0.5
                            yalign 0.0

                            if apps[i] == None:
                                pass
                            else:
                                add apps[i].icons[128] xalign 0.5
                                text _(apps[i].bundleName):
                                    style "ASDesktopLaunchpadViewAppText"
                                    xalign 0.5
