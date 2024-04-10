from data.db_connections import mongodb_context

def get_all_ships_details_from_db():
    db = mongodb_context.create_connection_with_db()
    collection = mongodb_context.get_the_ships_collection()
    ships_details = collection.find()
    for ship in ships_details:
        print(ship)
    

    