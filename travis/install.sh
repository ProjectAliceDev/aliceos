#!/bin/sh

#  install.sh
#  AliceOS
#
#  Created by Marquis Kurt on 7/4/19.
#  Copyright © 2019 ProjectAliceDev. All rights reserved.

renpy_version=$1

wget https://www.renpy.org/dl/$(renpy_version)/renpy-$(renpy_version)-sdk.tar.bz2
tar xf renpy-$(renpy_version)-sdk.tar.bz2
rm renpy-$(renpy_version)-sdk.tar.bz2
mv renpy-$(renpy_version)-sdk renpy
