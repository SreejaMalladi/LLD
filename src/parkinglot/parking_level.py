from parking_display_board import ParkingDisplayBoard
from models.parking_spot import ParkingSpotType


class ParkingLevel:
    def __init__(self, floor: int):
        self.__floor = floor
        self.__handicapped_spots = []
        self.__compact_spots = []
        self.__large_spots = []
        self.__motorcycle_spots = []
        self.__electric_spots = []
        self.__free_handicapped_spot_count = {'free_spot': 0}
        self.__free_compact_spot_count = {'free_spot': 0}
        self.__free_large_spot_count = {'free_spot': 0}
        self.__free_motorcycle_spot_count = {'free_spot': 0}
        self.__free_electric_spot_count = {'free_spot': 0}
        self.__display_board = ParkingDisplayBoard() 
        
        def add_parking_spot(self, spot):
            if spot.get_type() == ParkingSpotType.HANDICAPPED:
                self.__handicapped_spots.append(spot)
                self.__free_handicapped_spot_count['free_spot'] += 1
                self.__display_board.update_spot_count(spot.get_type(), self.__free_handicapped_spot_count["free_spot"])
            elif spot.get_type() == ParkingSpotType.COMPACT:
                self.__compact_spots.append(spot)
                self.__free_compact_spot_count['free_spot'] += 1
                self.__display_board.update_spot_count(spot.get_type(), self.__free_compact_spot_count)
            elif spot.get_type() == ParkingSpotType.LARGE:
                self.__large_spots.append(spot)
                self.__free_large_spot_count['free_spot'] += 1
                self.__display_board.update_spot_count(spot.get_type(), self.__free_large_spot_count)
            elif spot.get_type() == ParkingSpotType.MOTORCYCLE:
                self.__motorcycle_spots.append(spot)
                self.__free_motorcycle_spot_count['free_spot'] += 1
                self.__display_board.update_spot_count(spot.get_type(), self.__free_motorcycle_spot_count)
            elif spot.get_type() == ParkingSpotType.ELECTRIC:
                self.__electric_spots.append(spot)
                self.__free_electric_spot_count['free_spot'] += 1
                self.__display_board.update_spot_count(spot.get_type(), self.__free_electric_spot_count)
        