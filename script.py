from pytz import all_timezones, timezone
from github import Github
from datetime import datetime
import os
from dotenv import load_dotenv
#
# load_dotenv()

github_token = os.getenv('TOKEN')

repo_name = "EduardoProfe666/world-greetings"
file_path = "README.md"

g = Github(github_token)

repo = g.get_repo(repo_name)
contents = repo.get_contents(file_path)

file_content = \
    """
# World Greetings
This is basically a `python bot` that generates greetings every 15 minutes to
every part of the world.

## 🌎 Greetings

| **🎌 Part of the World/TimeZone** | **👋 Greeting** | **📅 Day** | **⌚Time** |
|---|---|---|---|
"""

for tz in all_timezones:
    t = datetime.now(timezone(tz))
    day = t.strftime('%A %d/%B/%Y')
    time = t.strftime('%I:%M %p')
    gr = "Good Evening"
    if 1 <= t.hour < 12:
        gr = "Good Morning"
    elif 12 <= t.hour < 18:
        gr = "Good Afternoon"

    file_content += f"| **{tz}** | {gr} | {day} | {time} |\n"
repo.update_file(contents.path, "Update grettings for all countries", file_content, contents.sha)


