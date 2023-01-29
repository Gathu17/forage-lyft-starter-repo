from abc import ABC
from car import Car
import datetime

class SpindlerBattery(Car,ABC):
    def __init__(self,last_service_date,current_date):
      super().__init__(last_service_date)
      self.current_date = datetime.date.today()