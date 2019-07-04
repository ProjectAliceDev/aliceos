#!/bin/sh

#  install.sh
#  AliceOS
#
#  Created by Marquis Kurt on 7/4/19.
#  Copyright © 2019 ProjectAliceDev. All rights reserved.

RENPY_VER=$1

wget https://www.renpy.org/dl/$(RENPY_VER)/renpy-$(RENPY_VER)-sdk.tar.bz2
tar xf renpy-$(RENPY_VER)-sdk.tar.bz2
rm renpy-$(RENPY_VER)-sdk.tar.bz2
mv renpy-$(RENPY_VER)-sdk renpy
