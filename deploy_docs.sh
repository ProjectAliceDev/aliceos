#!/bin/sh
#
# deploy_docs.sh
# (C) 2020 Project Alice.
# Licensed under BSD-2-Clause license
#
mkdocs build -d docs
echo "docs.aliceos.app" >> docs/CNAME
touch docs/.nojekyll