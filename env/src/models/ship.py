class Ship:
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
