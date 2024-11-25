import threading

from models.vehicle_type import VehicleType
from models.parking_spot import ParkingSpotTypeCount

from parking_ticket import ParkingTicket

class ParkingLot:
    instance = None
    
    class __OnlyOne:
        def __init__(self, name, address):
            self.__name = name
            self.__address = address
            self.__parking_rate = 5
            
            self.__compact_spot_count = 0
            self.__large_spot_count = 0
            self.__motorcycle_spot_count = 0
            self.__electric_spot_count = 0
            self.__handicapped_spot_count = 0
            
            self.__max_compact_spots = ParkingSpotTypeCount.COMPACT.value
            self.__max_large_spots = ParkingSpotTypeCount.LARGE.value
            self.__max_motorcycle_spots = ParkingSpotTypeCount.MOTORCYCLE.value
            self.__max_electric_spots = ParkingSpotTypeCount.ELECTRIC.value
            self.__max_handicapped_spots = ParkingSpotTypeCount.HANDICAPPED.value
            
            self.__parking_floors = {}
            
            self.__active_parking_tickets = {}
            self.__lock = threading.Lock()
            
        def __init__(self, name, address):
            
            if not ParkingLot.instance:
                ParkingLot.instance = ParkingLot.__OnlyOne(name, address)
            else:
                ParkingLot.instance.__name = name
                ParkingLot.instance.__address = address
            
        def get_instance(name, address):
            if not ParkingLot.instance:
                ParkingLot.instance = ParkingLot.__OnlyOne(name, address)
            return ParkingLot.instance
        
        def get_new_parking_ticket(self, vehicle):
            if self.is_full(vehicle.get_type()):
                raise Exception("Parking Full")
            
            self.__lock.acquire()
            ticket = ParkingTicket(vehicle, self.__parking_rate, self.get_empty_spot())
            self.__active_parking_tickets[ticket.get_ticket_number()] = ticket
            self.__lock.release()
            return ticket
        
        def get_empty_spot(self):
            for floor in self.__parking_floors.values():
                for spot in floor.get_parking_spots():
                    if spot.is_available():
                        return spot
            return None
            
        def is_full(self, vehicle_type):
            if vehicle_type == VehicleType.CAR:
                return self.__compact_spot_count + self.__large_spot_count >= self.__max_compact_spots + self.__max_large_spots
            elif vehicle_type == VehicleType.TRUCK:
                return self.__large_spot_count >= self.__max_large_spots
            elif vehicle_type == VehicleType.ELECTRIC:
                return self.__electric_spot_count >= self.__max_electric_spots
            elif vehicle_type == VehicleType.MOTORCYCLE:
                return self.__motorcycle_spot_count >= self.__max_motorcycle_spots
            return True
        
        