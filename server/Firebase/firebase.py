import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

import json
import os
from dotenv import load_dotenv
load_dotenv()

cred = credentials.Certificate(json.loads(os.getenv("firebase_config")))
firebase_admin.initialize_app(cred)


db = firestore.client()

submissions = db.collection(u'submissions')
comments = db.collection(u'comments')