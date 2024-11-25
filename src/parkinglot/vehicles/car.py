from vehicles.vehicle import Vehicle
from models.vehicle_type import VehicleType

class Car(Vehicle):
    def __init__(
        self,
        registration_number: int,
        color: str
        ):
        super().__init__(registration_number, color, VehicleType.CAR)
        
