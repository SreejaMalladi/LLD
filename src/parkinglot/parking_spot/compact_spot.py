from models.parking_spot import ParkingSpotType
from models.vehicle_type import VehicleType

from parking_spot import ParkingSpot


class CompactSpot(ParkingSpot):
    def __init__(
        self,
        spot_number: int,
    ):
        super().__init__(spot_number, VehicleType.CAR, ParkingSpotType.COMPACT)
    
    