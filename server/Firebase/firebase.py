import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./server/Firebase/secret/wallstreetbots-aa26c-firebase-adminsdk-vy7mv-b00e6a07e1.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

submissions = db.collection(u'submissions')
comments = db.collection(u'comments')