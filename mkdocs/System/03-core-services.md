#  Core Services

AliceOS comes with several bundled Core Services that you should be aware of. These Core Services are crucial to AliceOS's core and are included in every AliceOS installation. Core Services are given the `.aoscservice` file extension and exist under `System/CoreServices`.

!!! warning
    If you plan to remove a Core Service, do so with caution. Other parts of AliceOS may make system calls that heavily rely on them.

## Desktop

![Desktop icon](../images/system/cservices/desktop.png)

The Desktop Core Service is responsible for displaying current applications installed on the system as well as providing a desktop shell if necessary.
