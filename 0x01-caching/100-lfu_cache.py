#!/usr/bin/env python3
""" LFU Cache module """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching and implements a
    caching system with an LFU eviction policy.
    """

    def __init__(self):
        """ Initialize LFU cache """
        super().__init__()
        self.frequency = {}      # Track access frequency of each key
        self.usage_order = {}    # Track the order of access for each key

    def put(self, key, item):
        """
        Add an item in the cache.
        If the cache exceeds MAX_ITEMS, the least frequently
        used item is discarded.
        If there are multiple items with the same frequency,
        the LRU is discarded.
        """
        if key is None or item is None:
            return

        # Update or insert the item
        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            # Check if we need to discard an item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Find the LFU key, and if multiple, use the LRU key among them
                min_freq = min(self.frequency.values())
                lfu_keys = [k for k, v in self.frequency.items()
                            if v == min_freq]
                if len(lfu_keys) > 1:
                    # If there's a tie in frequency, use LRU to discard
                    lru_key = min(lfu_keys, key=lambda k: self.usage_order[k])
                else:
                    lru_key = lfu_keys[0]

                # Discard the chosen key
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                del self.usage_order[lru_key]
                print(f"DISCARD: {lru_key}")

            # Insert new key
            self.cache_data[key] = item
            self.frequency[key] = 1  # Set initial frequency count

        # Update usage order to current position
        self.usage_order[key] = len(self.usage_order)

    def get(self, key):
        """
        Get an item by key.
        If key exists, update its frequency and usage order.
        Returns None if key is None or if the key doesn’t exist in cache_data.
        """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and usage order for key access
        self.frequency[key] += 1
        self.usage_order[key] = len(self.usage_order)
        return self.cache_data[key]
