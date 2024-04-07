from pymongo import MongoClient
from data.db_connections.connection_data import Connection_Data

def create_connection_with_db():
    client = MongoClient(Connection_Data.CONNECTION_STRING)
    db = client[Connection_Data.DATABASE_NAME]
    return db

