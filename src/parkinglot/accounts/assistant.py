from models.account import Person, AccountType
from account import Account

class Assistant(Account):
    def __init__(self, username, password, person):
        super().__init__(username, password, person, AccountType.ASSISTANT)

    def process_ticket(self, ticket_number):
        pass
