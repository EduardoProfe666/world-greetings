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
    t = datetime.now(timezone(tz))
    day = t.strftime('%I:%M %p')
    time = t.strftime('%I:%M %p')
    gr = "Good Evening"
    if 1 <= t.hour < 12:
        gr = "Good Morning"
    elif 12 <= t.hour < 18:
        gr = "Good Afternoon"

    filename = f"greetings/{tz}.md"
    file_content = \
        f"""## 👋 {gr} `{tz}`
    ### 📅 Today is `{day}`
    ### ⌚ It's `{time}` there
    ### 🎩 With love, EduardoProfe666 
    """
    repo.
    repo.create_file(filename, "Add .md file for timezone", file_content)
