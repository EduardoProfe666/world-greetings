from pytz import all_timezones, timezone
from github import Github
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

github_token = os.getenv('GITHUB_TOKEN')

repo_name = "EduardoProfe666/world-greetings"
file_path = "greetings"

g = Github(github_token)

repo = g.get_repo(repo_name)

for tz in all_timezones:
    if "Cuba" in tz:
        print(datetime.now(timezone(tz)).strftime('%A %d/%B/%Y %I:%M %p'))
        break
