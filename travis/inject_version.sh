#!/bin/sh

# You find yourself in a strange place. This is where we inject semvering via Git Tags
# No need to change anything below the replacer variable.
# Just change the value of replacer, the script will do everything for you
 
replacer="0.1.2"

if [ ! -z $TRAVIS_TAG ]; then
  echo " ---> Tag exists, using tag."
  sed -i "s/define config.version = \"$replacer\"/define config.version = \"$TRAVIS_TAG\"/g" mod/game/options.rpy;
  cat mod/game/options.rpy | grep config.version;
else
  echo " ---> Tag not exists, using hash."
  sed -i "s/config.version = \"$replacer\"/config.version = \"$TRAVIS_COMMIT\"/g" mod/game/options.rpy;
  cat mod/game/options.rpy | grep config.version;
fi