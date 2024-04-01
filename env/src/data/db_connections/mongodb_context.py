from pymongo import MongoClient

def create_connection_with_db():
    CONNECTION_STRING = 'mongodb://localhost:27017'
    client = MongoClient(CONNECTION_STRING)
    db = client['shiptrackerdb']
    return db

