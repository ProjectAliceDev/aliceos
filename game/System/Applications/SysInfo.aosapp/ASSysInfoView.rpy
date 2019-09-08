#
# ASSysInfoView.rpy
# AliceOS
#
# Created by Marquis Kurt on 9/8/19.
# Copyright © 2019 ProjectAliceDev. All rights reserved.
#

init offset = 10

screen ASSysInfoView():

    frame:
        style "ASWindowFrame"
        xmaximum 800

        has vbox:
            style_prefix "ASVerticalBox"
            xalign 0.5
            yalign 0.5

            use ASWindowTitleBar("About AliceOS")

            null height 32

            hbox:
                spacing 32

                add ASSysInfoApp.bundleDir + "Resources/Elements/SystemIcon.png":
                    size (256, 256)
                    xoffset 16

                vbox:
                    text "AliceOS {=ASSysInfoTitle_text_nobold}[AS_SYS_INFO[COMMON_NAME]]{/}":
                        style "ASSysInfoTitle_text"
                    text "Version [AS_SYS_INFO[VERSION]] ([AS_SYS_INFO[BUILD_ID]])"
                    null height 16
                    text "{=ASSysInfoProperty_text_bold}Built for Ren'Py{/} 7.3.2.320":
                        style "ASSysInfoProperty_text"
                    null height 24
                    text "© 2018-2019 Project Alice.\nAliceOS is free and open-source software licensed under the BSD 2-Clause License.":
                        style "ASSysInfoCopyright_text"
                        yalign 1.0