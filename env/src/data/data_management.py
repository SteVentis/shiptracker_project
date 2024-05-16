import csv
from data.db_connections import mongodb_context
from shared.error import Error
from shared.result import Result

db = mongodb_context.create_connection_with_mongodb()
ships_collection = mongodb_context.get_the_ships_collection(db)
tracking_collection = mongodb_context.get_the_tracking_collection(db)

def insert_data_from_csv_to_mongodb(csv_filepath):
    ships_to_be_inserted_result = insert_ships_data(csv_filepath)
    print(ships_to_be_inserted_result)
    if ships_to_be_inserted_result.is_success:
        tracking_data_to_be_inserted_result = insert_tracking_data(csv_filepath)
        print(tracking_data_to_be_inserted_result)

def insert_ships_data(csv_filepath):
    ships_MMSI = ships_collection.distinct("MMSI")
    inserted_mmsi = set()
    try:
        with open(csv_filepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                mmsi = int(row.get('MMSI')) 
                if mmsi not in inserted_mmsi and mmsi not in ships_MMSI:
                    specific_columns = {
                            'MMSI': mmsi,
                            'VesselName': row.get('VesselName', ''),
                            'Heading': float(row.get('Heading', 0)),
                            'IMO': row.get('IMO', ''),
                            'CallSign': row.get('CallSign', ''),
                            'VesselType': int(row.get('VesselType', 0)) if row.get('VesselType', '').isdigit() else 0,
                            'Status': int(row.get('Status', 0)) if row.get('Status', '').isdigit() else 0,
                            'Length': float(row.get('Length', 0.0)) if row['Length'] != '' else 0.0,
                            'Width': float(row.get('Width', 0.0)) if row['Width'] != '' else 0.0,
                            'Draft': float(row.get('Draft', 0.0)) if row['Draft'] != '' else 0.0,
                            'Cargo': int(row.get('Cargo', 0)) if row.get('Cargo', '').isdigit() else 0,
                            'TranscieverClass': row.get('TranscieverClass', '')
                        }
                    ships_collection.insert_one(specific_columns)
                    inserted_mmsi.add(mmsi)
        return Result(True, Error.NONE)
    except Exception as e:
        return Result(False, Error.INSERT_DATA, e)

def insert_tracking_data(csv_filepath):
    try:
        with open(csv_filepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                specific_columns = {
                    'MMSI': int(row.get('MMSI', 0)),
                    'BaseDateTime': row.get('BaseDateTime', ''),
                    'LAT': float(row.get('LAT', 0.0)) if row['LAT'] != '' else 0.0,
                    'LON': float(row.get('LON', 0.0)) if row['LON'] != '' else 0.0,
                    'SOG': float(row.get('SOG', 0.0)) if row['SOG'] != '' else 0.0,
                    'COG': float(row.get('COG', 0.0)) if row['COG'] != '' else 0.0
                }
                tracking_collection.insert_one(specific_columns)
        return Result(True, Error.NONE)
    except Exception as e:
        return Result(False, Error.INSERT_DATA, e)