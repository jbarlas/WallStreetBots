from secret.praw_secret import reddit
from models import FirebaseSubmission
from firebase import comments

wsb = reddit.subreddit('wallstreetbets')

def comment_stream():
    for comment in wsb.stream.comments(skip_existing=True):
        print(comment)
        comments.add({
            'id': comment.id,
            'author_id': comment.author.id,
            'body': comment.body,
            'created_utc': comment.created_utc
        })

# for post in wsb.stream.submissions(limit=10):
#     posts.add({
#         'post_id': post.id,
#         'author': post.author.id,
#         'title': post.title, 
#         'text': post.selftext
#     })

def get_submission_by_id(id):
    return FirebaseSubmission(reddit.submission(id))

def get_submission_by_list(ids):
    """
    Takes in a list of submission ids and returns a list of FirebaseSubmission 
    """
    return [FirebaseSubmission(submission) for submission in reddit.info(["t3_" + id for id in ids])]


