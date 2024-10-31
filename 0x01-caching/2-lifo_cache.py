#!/usr/bin/env python3
""" LIFO Cache module """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and implements a
    caching system with a LIFO eviction policy.
    """

    def __init__(self):
        """ Initialize LIFO cache """
        super().__init__()
        self.last_key = None  # To keep track of the last key added

    def put(self, key, item):
        """
        Add an item in the cache.
        If the cache exceeds MAX_ITEMS, the last item added is discarded.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]

            self.cache_data[key] = item
            self.last_key = key

            # Check if cache size exceeds limit
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Discard the most recently added key
                del self.cache_data[self.last_key]
                print(f"DISCARD: {self.last_key}")
                self.last_key = key  # Update last_key for next use

    def get(self, key):
        """
        Get an item by key.
        Returns None if key is None or if the key doesn’t exist in cache_data.
        """
        return self.cache_data.get(key)
