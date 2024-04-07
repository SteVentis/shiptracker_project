from data import ship_repo
from resources import google_map

def get_ships_details():
    ship_repo.get_all_ships_details_from_db()