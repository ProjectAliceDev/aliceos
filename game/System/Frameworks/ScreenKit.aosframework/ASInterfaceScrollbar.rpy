# 
# ASInterfaceScrollbar.rpy
# AliceOS
# 
# Created by Marquis Kurt on 9/10/19
# Copyright © 2019 Marquis Kurt. All rights reserved.
#

style ASInterfaceScrollbar is viewport
style ASInterfaceScrollbar_text is ASInterface_text

style ASInterfaceScrollbar_vscrollbar:
    bar_vertical True
    bar_resizing False
    base_bar AS_FRAMEWORK_DIR("ScreenKit") + "Resources/Scrollbars/ScrollArea.png"
    thumb AS_FRAMEWORK_DIR("ScreenKit") + "Resources/Scrollbars/ScrollThumb.png"
    unscrollable "hide"
    yfit True