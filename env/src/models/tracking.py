class Tracking:
    """
    Tracking class for ships with the following attributes:
    - MMSI stands for Maritime Mobile Service Identities
    - The base date and time
    - LAT stands for Latitude
    - LOT stands for Longitude
    - SOG stands for speed over the ground
    - COG stands for Course over ground
    """
    def __init__(self, MMSI, BaseDateTime, LAT, LON, SOG, COG):
        self.MMSI = MMSI
        self.BaseDateTime = BaseDateTime
        self.LAT = LAT
        self.LON = LON
        self.SOG = SOG
        self.COG = COG
        
# μοντελοποίηση του tracking ενός πλοίου με κλάση Ship_tracking_model
