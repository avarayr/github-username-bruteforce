from itertools import permutations
from os import getenv
import sys
from API import *
from dotenv import load_dotenv
import utils
import time
from tqdm import tqdm
from UserCache import UserCache

load_dotenv()
personal_token = getenv('PERSONAL_TOKEN')

if not personal_token:
    print("Please define PERSONAL_TOKEN in the .env file (see .env.example)")
    print("Get it from https://github.com/settings/tokens")

cache = UserCache()

api = API(personal_token)

rate_limit = api.get_rate_limit()
remaining = rate_limit.remaining
limit = rate_limit.limit

arguments_len = len(sys.argv) - 1
n_letters = int(sys.argv[1]) if arguments_len > 0 else 2

print()
print(f'Using {n_letters} letter permutations')
print('———————————————————————————————————————')

permutations = utils.get_n_letter_permutations(n_letters)
possible_combinations = pow(26, n_letters)

print(f"You're about to check {possible_combinations} combinations")
print(f"Your rate limit is {remaining}/{limit}")

print()

decision = input('Continue? [y/n]: ')
if decision != 'y':
    quit()

total_i = 0
abandoned_i = 0
not_taken_i = 0

cache_dict = cache.getCacheDict()

cache_taken_active = cache_dict.get('taken_active')
cache_taken_inactive = cache_dict.get('taken_inactive')
cache_not_taken = cache_dict.get('not_taken')

force_save = False

for username in tqdm(permutations, total=possible_combinations):
    try:
        if cache.is_active(username) or cache.is_inactive(username) or cache.not_taken(username):
            continue

        fetch_user = api.get_user(username)

        if fetch_user != False:
            if fetch_user['is_abandoned']:
                tqdm.write(f'Found abandoned:  {username}')
                cache_taken_inactive.append(username)
                abandoned_i += 1
            else:
                cache_taken_active.append(username)
        else:
            tqdm.write(f'Found unused:  {username}')
            cache_not_taken.append(username)
            not_taken_i += 1
            

        total_i += 1
        time.sleep(0.05)
    except KeyboardInterrupt:
        tqdm.write('Quitting')
        force_save = True
    finally:
        if total_i % 10 == 0 or force_save:
          cache.save({
              "taken_active": cache_taken_active,
              "taken_inactive": cache_taken_inactive,
              "not_taken": cache_not_taken
          })
