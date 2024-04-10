import csv
from data.db_connections import mongodb_context
from shared.error import Error
from shared.result import Result


def insert_data_from_csv_to_mongodb(csv_filepath):
    db = mongodb_context.create_connection_with_mongodb()
    collection_name = mongodb_context.get_the_ships_collection(db)
    insert_ships_data(csv_filepath, collection_name)
    collection_tracking_name = mongodb_context.get_the_tracking_collection(db)
    insert_tracking_data(csv_filepath, collection_tracking_name)


def insert_ships_data(csv_filepath, ships_collection_name):
    inserted_mmsi = set()
    try:
        with open(csv_filepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                mmsi = row.get('MMSI')
                if mmsi not in inserted_mmsi:
                    specific_columns = {
                        'MMSI': int(mmsi) if mmsi.isdigit() else 0,
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
                    ships_collection_name.insert_one(specific_columns)
                    inserted_mmsi.add(mmsi)
        return Result(True, Error.NONE)
    except Exception as e:
        return Result(False, Error.INSERT_DATA, e)

def insert_tracking_data(csv_filepath, tracking_collection_name):
    try:
        with open(csv_filepath, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                specific_columns = {
                    'MMSI': int(row.get('MMSI', )),
                    'BaseDateTime': row.get('BaseDateTime', ''),
                    'LAT': float(row.get('LAT', 0.0)) if row['LAT'] != '' else 0.0,
                    'LON': float(row.get('LON', 0.0)) if row['LON'] != '' else 0.0,
                    'SOG': float(row.get('SOG', 0.0)) if row['SOG'] != '' else 0.0,
                    'COG': float(row.get('COG', 0.0)) if row['COG'] != '' else 0.0
                }
                tracking_collection_name.insert_one(specific_columns)
        return Result(True, Error.NONE)
    except Exception as e:
        return Result(False, Error.INSERT_DATA, e)