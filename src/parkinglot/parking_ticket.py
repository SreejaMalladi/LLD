import datetime

class ParkingTicket:
    
    def __init__(self):
        self.__ticket_number = None
        self.__vehicle = None
        self.__parked_spot = None
        self.__entry_time = None
        self.__exit_time = None
        self.__parking_rate = None
        self.__amount = None
        
    def create_parking_ticket(self, vehicle, parking_rate, spot):
        self.__vehicle = vehicle
        self.__parked_spot = spot
        self.__entry_time = datetime.datetime.now()
        self.__parking_rate = parking_rate
        self.__ticket_number = self.__generate_ticket_number()
        
        return self
    
    def close_parking_ticket(self):
        self.__exit_time = datetime.datetime.now()
        self.__amount = self.calculate_amount()
        
    def calculate_amount(self):
        time_difference = self.__exit_time - self.__entry_time
        time_difference_in_hours = time_difference.total_seconds() / 3600
        return self.__parking_rate() * time_difference_in_hours
    
    def __generate_ticket_number(self):
        return int(datetime.datetime.now().timestamp())
        