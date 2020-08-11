from dotenv import load_dotenv
from os import getenv
import random
import string
import datetime


from unittest import TestCase
from github import Github
from API import *


class API_(TestCase):
    def setUp(self):
        super().setUp()
        load_dotenv()
        self.personal_token = getenv('PERSONAL_TOKEN')
        self.API = API(self.personal_token)

    def testPersonalTokenLoads(self):
        assert self.personal_token is not None

    def testAPIIsInstantiated(self):
        assert self.API is not None

    def testGetUser(self):
        user = self.API.get_user('a')
        print(user)
        assert user['repo_count'] >= 0
        assert user['created_at'] == datetime.datetime(2012, 2, 5, 14, 53, 26)
        assert user['is_abandoned'] == False

    def testGetRateLimit(self):
        core = self.API.get_rate_limit()
        assert core.remaining >= 0
        assert core.limit >= 0

    def testNonexistantUser(self):
        longUsername = ''.join(random.choice(string.ascii_letters)
                               for i in range(63))
        assert self.API.get_user(longUsername) == False
