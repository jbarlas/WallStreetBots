from Firebase.firebase import submissions, comments
from Firebase.models import FirebaseSubmission, FirebaseComment

def add_submission(submission : FirebaseSubmission):
    submissions.document(f'{submission.id}').set(submission.to_dict())

def add_comment(comment : FirebaseComment):
    comments.document(f'{comment.id}').set(comment.to_dict())