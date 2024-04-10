from data import data_management
from resources import google_map

def get_ships_details():
    file_path ="C:\\Users\\venti\\Downloads\\AIS_2021_01_01\\AIS_2021_01_01.csv"
    data_management.insert_data_from_csv_to_mongodb(file_path)