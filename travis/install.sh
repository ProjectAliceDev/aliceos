#!/bin/sh

#  install.sh
#  AliceOS
#
#  Created by Marquis Kurt on 7/4/19.
#  Copyright © 2019 ProjectAliceDev. All rights reserved.

wget https://www.renpy.org/dl/$1/renpy-$1-sdk.tar.bz2
tar xf renpy-$1-sdk.tar.bz2
rm renpy-$1-sdk.tar.bz2
mv renpy-$1-sdk renpy
