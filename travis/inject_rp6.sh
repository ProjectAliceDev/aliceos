#!/bin/sh



sed -i "s/build.package(build.directory_name + \"_ASBaseSystem\", 'zip', build.name, description=\"AliceOS Base System Distributable\")/build.package(build.directory_name + \"_ASBaseSystem-rp6\", 'zip', build.name, description=\"AliceOS Base System Distributable\")/g" mod/game/options.rpy;
cat mod/game/options.rpy | grep build.package;
