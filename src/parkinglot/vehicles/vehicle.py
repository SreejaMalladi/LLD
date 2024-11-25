from abc import ABC
from models.vehicle_type import VehicleType

class Vehicle(ABC):
    def __init__(
        self,
        registration_number: int,
        color: str,
        vehicle_type: VehicleType
        ):
        self.registration_number = registration_number
        self.color = color
        self.vehicle_type = vehicle_type
        
    def get_registration_number(self) -> int:
        return self.registration_number
    
    def get_color(self) -> str:
        return self.color
    
    def get_vehicle_type(self) -> VehicleType:
        return self.vehicle_type
