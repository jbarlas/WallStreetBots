"""Logic for adding submissions to firebase"""

from Pushshift.pushshift_utils import Pushshift, PushshiftUrl
from PRAW.praw_utils import get_submission_by_id
from Firebase.firebase_utils import add_submission

def add_submissions():
    push = Pushshift(PushshiftUrl.SUBMISSION)
    push.set_query(size=5, subreddit="wallstreetbets", score=">10", sort="desc", sort_type="score", after=1577854800, before=1580274000)
    ids = push.gen_submission_ids()
    to_return = []
    for id in ids:
        submission = get_submission_by_id(id)
        to_return.append(submission.to_dict())
        print(submission.to_dict())
        add_submission(submission)
    return to_return
