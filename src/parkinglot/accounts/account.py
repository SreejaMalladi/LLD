from models.account import AccountStatus, Person, AccountType

class Account:
    def __init__(
        self,
        username: str,
        password: str,
        person: Person,
        role: AccountType.NONE,
        status: AccountStatus.ACTIVE
        ):
        self.username = username
        self.password = password
        self.person = person
        self.role = role
        self.status = status
        
    def reset_password(self) -> bool:
        pass
    
    def get_account_status(self) -> AccountStatus:
        return self.status
    
    def get_account_type(self) -> AccountType:
        return self.role
    
    def get_person(self) -> Person:
        return self.person