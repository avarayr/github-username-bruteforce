from github import Github
import datetime


class API:

    def __init__(self, personal_token):
        self.github = Github(login_or_token=personal_token)

    def get_user(self, username: str):
        try:
            profile = self.github.get_user(username)
            repo_count = profile.get_repos().totalCount
            return {
                'repo_count': repo_count,
                'created_at': profile.created_at,
                'updated_at': profile.updated_at,
                'is_abandoned': (datetime.datetime.now() - profile.updated_at).days > 365 * 5
                and repo_count == 0
            }
        except:
            return False

    def get_rate_limit(self):
        rate_limit = self.github.get_rate_limit()
        core = rate_limit.core
        return core
