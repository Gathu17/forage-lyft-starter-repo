import unittest
from datetime import datetime

from engine.capulet_engine import Capulet
from engine.sternman_engine import Sternman
from engine.willoughby_engine import Willoughby
from battery.nubbin_battery import Nubbin
from battery.spindler_battery import Spindler

class TestNubbin(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)
        current_date = datetime.today().date()

        battery = Nubbin(last_service_date, current_date)
        self.assertTrue(battery.needs_service())
  
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
        current_date = datetime.today().date()

        battery = Nubbin(last_service_date, current_date)
        self.assertFalse(battery.needs_service())
    
class TestSpindler(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_date = datetime.today().date()

        battery = Spindler(last_service_date, current_date)
        self.assertTrue(battery.needs_service())
    
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        current_date = datetime.today().date()

        battery = Spindler(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 300001
        last_service_mileage = 0

        engine = Capulet(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 29000
        last_service_mileage = 0

        engine = Capulet(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 600001
        last_service_mileage = 0

        engine = Willoughby(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        current_mileage = 59000
        last_service_mileage = 0

        engine = Willoughby(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

class TestSternamnEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = True

        engine = Sternman(last_service_date, warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        warning_light_is_on = False

        engine = Sternman(last_service_date, warning_light_is_on)
        self.assertFalse(engine.needs_service())


if __name__ == '__main__':
    unittest.main()
