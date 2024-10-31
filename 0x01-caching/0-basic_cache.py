#!/usr/bin/env python3
""" BasicCache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and implements a basic
    caching system without any size limit.
    """

    def put(self, key, item):
        """
        Add an item in the cache.
        If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key.
        Returns None if key is None or if the key doesn’t exist in cache_data.
        """
        return self.cache_data.get(key)
