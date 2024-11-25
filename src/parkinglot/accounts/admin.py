from models.account import AccountType
from account import Account

class Admin(Account):
    def __init__(self, username, password, person):
        super().__init__(username, password, person, AccountType.ADMIN)

    def add_parking_floor(self, floor):
        pass
    
    def add_parking_spot(self, floor_name, spot):
        pass
    
    def add_parking_display_board(self, floor_name, display_board):
        pass
    
    def add_customer_info_panel(self, floor_name, info_panel):
        pass
    
    def add_entrance_panel(self, floor_name, entrance_panel):
        pass