#!/bin/sh

#  install.sh
#  AliceOS
#
#  Created by Marquis Kurt on 7/4/19.
#  Copyright © 2019 ProjectAliceDev. All rights reserved.

RPVER="$1"

wget https://www.renpy.org/dl/$(RPVER)/renpy-$(RPVER)-sdk.tar.bz2
tar xf renpy-$(RPVER)-sdk.tar.bz2
rm renpy-$(RPVER)-sdk.tar.bz2
mv renpy-$(RPVER)-sdk renpy
