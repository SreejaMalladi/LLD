from enum import Enum

class AccountStatus(Enum):
    ACTIVE = 1
    CLOSED = 2
    CANCELED = 3
    BLACKLISTED = 4
    NONE = 5

class AccountType(Enum):
    ADMIN = 1
    ASSISTANT = 2
    NONE = 3

class Address:
    def __init__(self, street, city, state, zip_code, country):
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__country = country
        
class Person:
    def __init__(self, name, address, email, phone):
        self.__name = name
        self.__address = address
        self.__email = email
        self.__phone = phone
