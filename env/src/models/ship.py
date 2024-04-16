class Ship:
    """
    Ship class for ships with the following attributes:
    - MMSI stands for Maritime Mobile Service Identities
    - Name of the Vessel
    - Heading of the vessel
    - IMO of the vessel
    - CallSign of the vessel
    - Type of the vessel
    - Status of the vessel
    - Lenght of the vessel
    - Width of the vessel
    - Draft for the vessel
    - Cargo of the vessel
    - TranscieverClass of the vessel
    
    """
    def __init__(self, MMSI, VesselName, Heading, IMO, CallSign, VesselType, Status, Length, Width, Draft, Cargo, TranscieverClass):
        self.MMSI = MMSI
        self.VesselName = VesselName
        self.Heading = Heading
        self.IMO = IMO
        self.CallSign = CallSign
        self.VesselType = VesselType
        self.Status = Status
        self.Length = Length
        self.Width = Width
        self.Draft = Draft
        self.Cargo = Cargo
        self.TranscieverClass = TranscieverClass
        
# μοντελοποίηση του αντικειμένου "πλοίο" μεσω της κλάσης Ship