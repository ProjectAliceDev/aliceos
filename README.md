![AliceOS header](repo_assets/project_header.png)

![AliceOS 2.0.0](https://img.shields.io/badge/aliceos-2.0.0-yellow.svg) [![Build Status](https://travis-ci.com/alicerunsonfedora/CatalinaToriel.svg?token=d7YdxjzD7RWGCxysa2ip&branch=master)](https://travis-ci.com/alicerunsonfedora/CatalinaToriel)

A modern rewrite of the AliceOS framework

## About this project

This project aims to rewrite the existing AliceOS framework and add new features for developers and users of AliceOS in any Ren'Py project to enjoy. The objectives are simple:

- **Focus on modularity**: AliceOS has always been bundled as a complete package, but not every Ren'Py developer wants to include a full AliceOS distribution. The aim to fix this is with a new framework format, under the `.aosframework` format. These frameworks are placed in the `System/Frameworks` folder and are not heavily reliant on AppKit.aosframework. However, the definitions file that states the default directories and what-not must be included in the System folder (including fonts).
- **Write better APIs**: Though AliceOS's APIs have made sense, they don't necessary make for the most elegant solution on the planet. The rewrite aims to write APIs and code similar to that of macOS and iOS.
- **Safer by default**: AliceOS has always strived to make applets safer by including a security system, however this system hasn't been fully implemented. The aim is to include all of these security features by _default_ in AppKit.aosframework. For full efficiency, apps using this framework should use only the functions provided by that framework to obey user requests.
- **All contained in one place**: The older versions of AliceOS had their directories completely exposed in the `game` folder of Ren'Py projects, which was a little too messy. This rewrite tries to fix it by following a folder structure similar to macOS with System, Applications, etc.
- **Faster installation**: To install AliceOS before, developers needed to clone the source code and configure build settings accordingly. This rewrite aims to fix this by distributing only a Ren'Py archive to developers and letting them build on top of that, meaning less work on the developer.

## Build instructions
To build this project, clone the repository and in Ren'Py Launcher, click "Distribute" and select "AliceOS Base System Distributable". The resulting file will be in a ZIP archive with `AliceOSBaseSystem.rpa`.

## Install instructions (to existing projects)
To install AliceOS directly without grabbing the source, download the ZIP archive from the release and copy `AliceOSBaseSystem.rpa` to your `game` folder.
