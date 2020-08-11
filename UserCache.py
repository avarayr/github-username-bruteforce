from json.decoder import JSONDecodeError
import os
import json


class UserCache():
    def __init__(self, cache_filename='_cache.json'):
        self.cache_filename = cache_filename
        if not os.path.exists(cache_filename):
            open(cache_filename, 'w').close()
        self.cache_file = open(cache_filename, 'r')
        self.cache = None
        self._load()

    def getCacheDict(self):
        return self.cache

    def save(self, obj_dict):
        with open(self.cache_filename, 'w+') as cache_file:
            json.dump(obj_dict, cache_file)

    def _load(self):
        try:
            self.cache = json.load(self.cache_file)
        except JSONDecodeError:
            self.cache = {
                "taken_active": [],
                "taken_inactive": [],
                "not_taken": []
            }

    def is_active(self, username):
        if (self.cache is None):
            self._load()

        return username in self.cache.get('taken_active', [])

    def is_inactive(self, username):
        if (self.cache is None):
            self._load()

        return username in self.cache.get('taken_inactive', [])

    def not_taken(self, username):
        if (self.cache is None):
            self._load()

        return username in self.cache.get('not_taken', [])
