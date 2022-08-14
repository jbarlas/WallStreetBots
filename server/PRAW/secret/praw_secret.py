import praw
import os

from dotenv import load_dotenv
load_dotenv()

reddit = praw.Reddit(client_id="ja2u91jkLhK_vy3wdh4-9A",
                    client_secret=os.getenv("client_secret"),
                    user_agent="WallStreetBots")
