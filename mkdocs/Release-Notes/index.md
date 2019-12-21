#  Prospect Park (2.0.0) Developer Beta 4

The following document covers the latest changes in AliceOS Prospect Park (v. 2.0.0).

## Inventories

- `ASInventoryItem` objects can now have an optional ID field, `itemId`.
- `ASInventories` includes new methods:
    - `export(filter=None)`: Return the inventory with a filter, if specified.
    - `getItemById(itemId)`: Find an item by its ID.

## AppKit

- Permission strings now reference App Manager instead of Settings.

## Desktop

- `showDesktop()` now calls `renpy.show_screen` instead of `renpy.call_screen`. For the old behavior, reference `_callDesktop()`.

## CI/CD

- AliceOS now produces builds on every push/pull request that can be accessed on GitHub Actions.

!!! warning
    Treat these builds from GitHub as a developer release; do _not_ use these builds in production-ready visual novels.