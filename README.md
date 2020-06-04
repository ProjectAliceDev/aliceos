![AliceOS header](repo_assets/project_header.png)

[![Latest release](https://img.shields.io/github/v/release/projectalicedev/aliceos)](https://github.com/projectalicedev/aliceos/releases) ![Build Status](https://github.com/ProjectAliceDev/aliceos/workflows/Build%20AliceOS%20Archive/badge.svg) ![Lint Status](https://github.com/ProjectAliceDev/aliceos/workflows/Lint/badge.svg)

AliceOS is a robust, evolving Ren'Py framework by Project Alice that adds an operating system-like experience to visual novel projects. AliceOS is easy to install, extendable, and is great for adding another layer of interactivity to your games.

> :warning: The following branch is dedicated to the next release of AliceOS after AliceOS Prospect Park. Features and improvements will change over time.

## Core principles

The core principles of AliceOS are:

- **Modular**: AliceOS uses a new framework format, under the `.aosframework` format. These frameworks are placed in the `System/Frameworks` folder and are not heavily reliant on AppKit.aosframework. However, the definitions file that states the default directories and what-not must be included in the System folder (including fonts).
- **Apple-style APIs**: AliceOS's APIs aim to be easy-to-use and familiar to developers that have worked with APIs for macOS, iOS, tvOS, and watchOS.
- **Safely extensible**: AliceOS includes support for extending itself with apps that are protected using appropriate, official APIs.
- **Easy-to-install**: AliceOS installation is as easy as just copying the Ren'Py archive over to the game folder.

## Build instructions

To build this project, clone the repository and in Ren'Py Launcher, click "Distribute" and select "AliceOS Base System Distributable". The resulting file will be in a ZIP archive with `AliceOSBaseSystem.rpa`.

## Install instructions (to existing projects)

To install AliceOS directly without grabbing the source, download the ZIP archive from the release and copy `AliceOSBaseSystem.rpa` to your `game` folder.

Additional instructions can be found in the [documentation](https://nextdocs.aliceos.app/01-install/).

## Documentation build instructions

To generate the documentation site (requires MkDocs and Material for MkDocs):

```bash
mkdocs build -d docs
```
