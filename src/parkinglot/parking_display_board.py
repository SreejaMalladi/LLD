from models.parking_spot import ParkingSpotType

class ParkingDisplayBoard:
    def __init__(self, id):
        self.id = id
        self.handicapped_free_spot = None
        self.compact_free_spot = None
        self.large_free_spot = None
        self.motorcycle_free_spot = None
        self.electric_free_spot = None
        
    def show_empty_spot_number(self):
        message = ""
        message += "Free Handicapped: " + str(self.handicapped_free_spot) + " "
        message += "Free Compact: " + str(self.compact_free_spot) + " "
        message += "Free Large: " + str(self.large_free_spot) + " "
        message += "Free Motorcycle: " + str(self.motorcycle_free_spot) + " "
        message += "Free Electric: " + str(self.electric_free_spot) + " "
        print(message)
        
    def update_spot_count(self, spot_type, count):
        if spot_type == ParkingSpotType.HANDICAPPED:
            self.handicapped_free_spot = count['free_spot']
        elif spot_type == ParkingSpotType.COMPACT:
            self.compact_free_spot = count['free_spot']
        elif spot_type == ParkingSpotType.LARGE:
            self.large_free_spot = count['free_spot']
        elif spot_type == ParkingSpotType.MOTORCYCLE:
            self.motorcycle_free_spot = count['free_spot']
        elif spot_type == ParkingSpotType.ELECTRIC:
            self.electric_free_spot = count['free_spot']