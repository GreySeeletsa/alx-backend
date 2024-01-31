#!/usr/bin/env python3
"""Module for task 0.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """A caching system that inherits from BaseCaching and does not have a
    limit on the num of items it can store
    """
    def put(self, key, item):
        """Assigns the item value to the key in the dictionary self.cache_data
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key, None)
