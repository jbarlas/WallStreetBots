from firebase import submissions, comments
from models import FirebaseSubmission, FirebaseComment
from firebase_admin import firestore

def add_submission(submission : FirebaseSubmission):
    submissions.document(f'{submission.id}').set(submission.to_dict())

def add_comment(comment : FirebaseComment):
    comments.document(f'{comment.id}').set(comment.to_dict())

def all_submissions():
    all_submissions = submissions.stream()
    to_return = []
    for submission in all_submissions:
        to_return.append(submission.to_dict())
    return to_return

def get_recent_submission(num_submissions=1):
    subs = submissions.order_by('created_utc', direction=firestore.Query.DESCENDING).limit(num_submissions).get()
    return [s.to_dict() for s in subs]