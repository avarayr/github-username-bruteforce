from UserCache import *
from unittest import TestCase


class Cache(TestCase):
    def setUp(self):
        super().setUp()
        self.cache = UserCache('tests/_test_cache.json')

    def testIsActive(self):
        assert self.cache.is_active('avarayr')

    def testIsInActive(self):
        assert self.cache.is_inactive('not_avarayr')
      
    def testNotTaken(self):
        assert self.cache.not_taken('avarayr_not_taken')
