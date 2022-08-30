"""Logic for adding submissions to firebase"""

from pushshift_utils import Pushshift, PushshiftUrl
from praw_utils import get_submission_by_id
from firebase_utils import add_submission, all_submissions, get_recent_submission

from datetime import datetime, timedelta

from praw_utils import get_submission_by_list

def add_submissions_by_day(time, subreddit="wallstreetbets", size=100):
    push = Pushshift(PushshiftUrl.SUBMISSION)
    day_after = time + 86400 
    push.set_query(size=size, subreddit=subreddit, sort="desc", sort_type="score", after=time, before=day_after)
    ids = push.gen_submission_ids()
    submissions = get_submission_by_list(ids)
    to_return = {
        "data": [submision.to_dict() for submision in submissions],
        "next_utc": day_after,
    }
    return to_return

def submission_history():
    return all_submissions()

def recent_submission():
    return get_recent_submission()