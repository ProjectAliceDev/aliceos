#!/bin/bash

# You find yourself in a strange place. This is where we inject semvering via Git Tags
# No need to change anything below the replacer variable.
# Just change the value of replacer, the script will do everything for you

replacer="2.0.0"
shortened_hash="$(echo $TRAVIS_COMMIT | head -c 7)"

if [[ $TRAVIS_TAG == "ref/tags"* ]]; then
    tag_remove="ref/tags"
    NEW_TRAVIS_TAG=${TRAVIS_TAG#tag_remove}
    TRAVIS_TAG=NEW_TRAVIS_TAG
fi

if [ ! -z $TRAVIS_TAG ]; then
  echo "Tag ${TRAVIS_TAG} found. Using tag..."
  sed -i "s/define config.version = \"$replacer\"/define config.version = \"$TRAVIS_TAG\"/g" game/options.rpy;
  sed -i "s/\"BUILD_ID\": \"GITHASH\"/\"BUILD_ID\":  \"$TRAVIS_TAG\"/g" game/System/ASDefinitions.rpy;
  cat game/options.rpy | grep config.version;
  cat game/System/ASDefinitions.rpy | grep BUILD_ID;
else
  echo "No tag found. Using Git hash..."
  sed -i "s/config.version = \"$replacer\"/config.version = \"$shortened_hash\"/g" game/options.rpy;
  sed -i "s/\"BUILD_ID\": \"GITHASH\"/\"BUILD_ID\":  \"$shortened_hash\"/g" game/System/ASDefinitions.rpy;
  cat game/options.rpy | grep config.version;
  cat game/System/ASDefinitions.rpy | grep BUILD_ID;
fi
