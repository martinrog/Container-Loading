from BinPacker.Constants import RotationType
from BinPacker.aux_methods import set_to_decimal

class Box:
    def __init__(self, name, width, height, length, weight):
        self.name = name
        self.width = width
        self.height = height
        self.length = length
        self.weight = weight
        self.rotation_type = 0
        self.position = [0, 0, 0]
        self.number_of_decimals = 3

    def format_numbers(self, number_of_decimals):
        """This function rounds the numbers of the measurements"""
        self.width = set_to_decimal(self.width, number_of_decimals)
        self.height = set_to_decimal(self.height, number_of_decimals)
        self.length = set_to_decimal(self.length, number_of_decimals)
        self.weight = set_to_decimal(self.weight, number_of_decimals)
        self.number_of_decimals = number_of_decimals

    def string(self):
        return "%s (%sx%sx%s, weight: %s) pos(%s) rt(%s) vol(%s)" % (
            self.name, self.width, self.height, self.length, self.weight,
            self.position, self.rotation_type, self.get_volume()
        )

    def string(self):
        return f"{self.name} : ({self.width}x{self.height}x{self.length}, weight: {self.weight}) | Volume: {self.get_volume()} CBM | pos({self.position}) | rt({self.rotation_type})"

    def get_volume(self):
        return set_to_decimal(
            self.width * self.height * self.length, self.number_of_decimals
        )

    def get_dimension(self):
        if self.rotation_type == RotationType.RT_WHD:
            dimension = [self.width, self.height, self.length]
        elif self.rotation_type == RotationType.RT_HWD:
            dimension = [self.height, self.width, self.length]
        elif self.rotation_type == RotationType.RT_HDW:
            dimension = [self.height, self.length, self.width]
        elif self.rotation_type == RotationType.RT_DHW:
            dimension = [self.length, self.height, self.width]
        elif self.rotation_type == RotationType.RT_DWH:
            dimension = [self.length, self.width, self.height]
        elif self.rotation_type == RotationType.RT_WDH:
            dimension = [self.width, self.length, self.height]
        else:
            dimension = []

        return dimension