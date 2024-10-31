#!/usr/bin/env python3
""" MRU Cache module """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache inherits from BaseCaching and implements a
    caching system with an MRU eviction policy.
    """

    def __init__(self):
        """ Initialize MRU cache """
        super().__init__()
        self.usage_order = []  # Track the order of usage for keys

    def put(self, key, item):
        """
        Add an item in the cache.
        If the cache exceeds MAX_ITEMS, the most recently used item is
        discarded.
        """
        if key is not None and item is not None:
            # Remove key if it already exists to update usage order
            if key in self.cache_data:
                self.usage_order.remove(key)
            self.cache_data[key] = item
            self.usage_order.append(key)

            # Check if cache size exceeds limit
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                # Discard the most recently used item
                mru_key = self.usage_order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

    def get(self, key):
        """
        Get an item by key.
        If key exists, move it to the end to mark it as recently used.
        Returns None if key is None or if the key doesn’t exist in cache_data.
        """
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end to mark it as recently used
        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
