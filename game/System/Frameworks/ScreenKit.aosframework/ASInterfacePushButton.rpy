# 
# ASInterfacePushButton.rpy
# AliceOS
# 
# Created by Marquis Kurt on 9/9/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

style ASInterfacePushButton is gui_button:
    background Frame([AS_FRAMEWORK_DIR("ScreenKit") + "Resources/Buttons/PushButtonIdle.png"], Borders(20, 8, 20, 8), tile=False)
    hover_background Frame([AS_FRAMEWORK_DIR("ScreenKit") + "Resources/Buttons/PushButtonHover.png"], Borders(20, 8, 20, 8), tile=False)
    padding(20, 8)

style ASInterfacePushButton_text is ASInterface_button_text:
    color "#212121"
    size 16