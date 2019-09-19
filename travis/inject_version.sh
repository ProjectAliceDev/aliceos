#!/bin/sh

# You find yourself in a strange place. This is where we inject semvering via Git Tags
# No need to change anything below the replacer variable.
# Just change the value of replacer, the script will do everything for you
 
replacer="2.0.0"
shortened_hash="$(echo $TRAVIS_COMMIT | head -c 7)"

if [ ! -z $TRAVIS_TAG ]; then
  echo " ---> Tag exists, using tag."
  sed -i "s/define config.version = \"$replacer\"/define config.version = \"$TRAVIS_TAG\"/g" mod/game/options.rpy;
  sed -i "s/\"BUILD_ID\": \"GITHASH\"/\"BUILD_ID\":  \"$TRAVIS_TAG\"/g" mod/game/System/ASDefinitions.rpy;
  cat mod/game/options.rpy | grep config.version;
  cat mod/game/System/ASDefinitions.rpy | grep BUILD_ID;
else
  echo " ---> Tag not exists, using hash."
  sed -i "s/config.version = \"$replacer\"/config.version = \"$shortened_hash\"/g" mod/game/options.rpy;
  sed -i "s/\"BUILD_ID\": \"GITHASH\"/\"BUILD_ID\":  \"$shortened_hash\"/g" mod/game/System/ASDefinitions.rpy;
  cat mod/game/options.rpy | grep config.version;
  cat mod/game/System/ASDefinitions.rpy | grep BUILD_ID;
fi
