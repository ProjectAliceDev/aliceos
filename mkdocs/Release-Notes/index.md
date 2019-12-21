#  Prospect Park (2.0.0) Developer Beta 4

The following document covers the latest changes in AliceOS Prospect Park (v. 2.0.0).
## Inventories

- `ASInventoryItem` objects can now have an optional ID field, `itemId`.
- `ASInventories` includes new methods:
    - `export(filter=None)`: Return the inventory with a filter, if specified.
    - `getItemById(itemId)`: Find an item by its ID.