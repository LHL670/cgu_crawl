import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def db():
    if not firebase_admin._apps:
        cred = credentials.Certificate("jsonFile/service-account.json")
        firebase_admin.initialize_app(cred)

    db = firestore.client()
    return db
