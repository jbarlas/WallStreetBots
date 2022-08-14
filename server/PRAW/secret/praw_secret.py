import praw
import os

from dotenv import load_dotenv
load_dotenv()

reddit = praw.Reddit(client_id="ewXab7fd6IRYg-H6alAx7g",
                    client_secret=os.getenv("client_secret"),
                    user_agent="wsb_scraper")
