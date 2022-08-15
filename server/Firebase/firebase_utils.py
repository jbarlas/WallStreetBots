from Firebase.firebase import submissions, comments
from Firebase.models import FirebaseSubmission, FirebaseComment
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

def get_recent_submission():
    return submissions.orderBy('created_utc', direction=firestore.Query.DESCENDING).limit(1)