#  Bootloader

![Bootloader logo](../images/system/bootloader.png)

The bootloader is responsible for displaying a boot screen while important components are loading. The bootloader is cusomizable with a certain timeout, depending on how fast you want the OS to "load".

## Available methods

### `$ ASBootloader.boot(timeout=5)`

Show the bootloader for a certain amount of time.

**Parameters**

- `tiemout`: The amount of seconds to show the bootloader for.
