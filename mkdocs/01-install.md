#  Getting Started

This document will help you get started with installing AliceOS and attaching it to your Ren'Py project.

## Downloading the base system

If you do not plan to customize AliceOS too much, you can add the base system archive and use AliceOS that way.

Download the latest release from the Downloads page and extract the ZIP archive. Then, copy `AliceOSBaseSystem.rpa` over to your Ren'Py project's game folder.

!!! warning "About using AliceOS with DDLC"
    If you plan to use AliceOS in a mod for Doki Doki Literature Club!, you must make sure that the base system version that you use is built against Ren'Py **6.99.12.4** to maintain compatibility.
    
    The release ZIP file is generally noted as 'AliceOS-x.x.x-_AliceOSBaseSystem-rp6.zip'.

## Building from source code

Alternatively, you can build `AliceOSBaseSystem.rpa` yourself with the customization you need.

1. Download the source code for the particular release you'd like and open Ren'Py Launcher.
2. Select the AliceOS source code and click "Build Distributions".
3. Uncheck the distribution options and check "Alice OS Base System Distributable".
4. Click "Build".

Your resulting ZIP file will be located in `AliceOS-x.x.x-dists`, and you can follow the instructions from **Downloading the base system** to finalize installation.

!!! warning "About building AliceOS for DDLC use"
    If you plan to build AliceOS for a Doki Doki Literature Club! mod, you must make sure that you use Ren'Py SDK v**6.99.12.4** to maintain compatibility.
