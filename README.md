# Github Permutation Username Finder ✨ 

Find unused and abandoned usernames by bruteforcing all letter combinations. **Requires a personal access api (with a view user permission)**

## Requirements ℹ️ 

- Python 3.x
- Pip
- Github personal access API key

## Rate limit warning ⚠️
Github has a 5000 requests/hr rate limit. The script will show the remaining requests you have available.

## Usage

1. `pip3 install -r requirements.txt`
2. Create a file named `.env`. Follow the example in the `.env.example` file to insert your own personal access key.
3. `python3 permutations.py [number of letters]`
4. Find results in the **cache.json** file


Example:
 
```bash
python3 permutations.py 2
```

If `number of letters` is not set, 2 is the default value.


### Bonus
* [Github Name Squatting policy](https://docs.github.com/en/github/site-policy/github-username-policy) 👀

* [Github Contact Link](https://support.github.com/contact) 🥳