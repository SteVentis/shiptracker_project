from data.db_connections import sqlitedb_context
from data.db_connections import mongodb_context
from models import ship

def get_all_ships_details_from_db():
    db = mongodb_context.create_connection_with_db()
    collection = db['ships_details']
    ships_details = collection.find()
    for ship in ships_details:
        print(ship)
    
