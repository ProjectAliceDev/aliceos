#!/usr/bin/env sh
if [[ $TRAVIS_TAG == "ref/tags"* ]]; then
    tag_remove="ref/tags"
    NEW_TRAVIS_TAG=${TRAVIS_TAG#tag_remove}
    TRAVIS_TAG=NEW_TRAVIS_TAG
fi
echo $TRAVIS_TAG