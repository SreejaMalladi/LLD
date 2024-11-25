from enum import Enum

class ParkingSpotType(Enum):
    HANDICAPPED = 1
    LARGE = 2
    COMPACT = 3
    MOTORCYCLE = 4
    ELECTRIC = 5

class ParkingSpotStatus(Enum):
    OCCUPIED = 1
    FREE = 2
    
class ParkingSpotTypeCount(Enum):
    HANDICAPPED = 5
    LARGE = 10
    COMPACT = 30
    MOTORCYCLE = 10
    ELECTRIC = 15