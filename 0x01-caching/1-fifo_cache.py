#!/usr/bin/env python3
""" FIFO Cache module """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and implements a
    caching system with a FIFO eviction policy.
    """

    def __init__(self):
        """ Initialize FIFO cache """
        super().__init__()
        self.order = []  # To track the order of insertion

    def put(self, key, item):
        """
        Add an item in the cache.
        If the cache exceeds MAX_ITEMS, the first item added is discarded.
        """
        if key is not None and item is not None:
            # If key is already in cache, remove it from order
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)

            # Check if cache size exceeds limit
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Remove the first added item
                first_in_key = self.order.pop(0)
                del self.cache_data[first_in_key]
                print(f"DISCARD: {first_in_key}")

    def get(self, key):
        """
        Get an item by key.
        Returns None if key is None or if the key doesn’t exist in cache_data.
        """
        return self.cache_data.get(key)
