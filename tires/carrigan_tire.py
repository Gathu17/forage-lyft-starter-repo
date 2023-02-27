from abc import ABC
from car import Car

class Carrigan(Car,ABC):
    def __init__(self,tires_array):
        self.tires_array = tires_array

    def needs_service(self):
        result = False
        for x in self.tires_array:
            if x >= 0.9:
                result =  True
        
        return result