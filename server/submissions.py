"""Logic for adding submissions to firebase"""

from pushshift_utils import Pushshift, PushshiftUrl
from praw_utils import get_submission_by_id
from firebase_utils import add_submission, all_submissions, get_recent_submission

def add_submissions_by_day(time, subreddit="wallstreetbets", size=100):
    push = Pushshift(PushshiftUrl.SUBMISSION)
    day_after = time + 86400 
    push.set_query(size=size, subreddit=subreddit, sort="desc", sort_type="score", after=time, before=day_after)
    ids = push.gen_submission_ids()
    data = []
    for id in ids:
        submission = get_submission_by_id(id)
        data.append(submission.to_dict())
        print(submission.to_dict()["title"])
        add_submission(submission)
    to_return = {
        "data": data,
        "next_utc": day_after
    }
    return to_return

def submission_history():
    return all_submissions()

def recent_submission():
    return get_recent_submission()