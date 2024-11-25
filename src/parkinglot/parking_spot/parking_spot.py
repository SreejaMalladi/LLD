from models.vehicle_type import VehicleType
from vehicles.vehicle import Vehicle
from models.parking_spot import ParkingSpotStatus, ParkingSpotType

class ParkingSpot:
    def __init__(
        self,
        spot_number: int,
        vehicle_type: VehicleType,
        parking_spot_type: ParkingSpotType
    ):
        self.spot_number = spot_number
        self.vehicle_type = VehicleType.CAR,
        self.parked_vehicle = None,
        self.spot_status = ParkingSpotStatus.FREE
        self.parking_spot_type = ParkingSpotType.COMPACT
        
    def is_available(self) -> bool:
        return self.spot_status == ParkingSpotStatus.FREE
    
    def park_vehicle(self, vehicle: Vehicle, spot_type: ParkingSpotType) -> None:
        if self.is_available():
            if vehicle.get_vehicle_type() == self.vehicle_type:
                self.spot_status = ParkingSpotStatus.OCCUPIED
                self.parked_vehicle = vehicle
                self.vehicle_type = vehicle.get_vehicle_type()
            else:
                raise Exception("Invalid Vehicle Type")
        else:
            raise Exception("Parking Spot is already occupied")
    
    def remove_vehicle(self) -> None:
        if not self.is_available():
            self.spot_status = ParkingSpotStatus.FREE
            self.parked_vehicle = None
            self.vehicle_type = VehicleType.CAR
        else:
            raise Exception("Parking Spot is already free")
        
    def get_spot_number(self) -> int:
        return self.spot_number
    
    def get_parked_vehicle(self) -> Vehicle:
        return self.parked_vehicle
    
    def get_spot_status(self) -> ParkingSpotStatus:
        return self.spot_status
    
    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type
    
    def get_parking_spot_type(self) -> ParkingSpotType:
        return self.parking_spot_type