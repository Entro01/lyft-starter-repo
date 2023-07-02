from car import Car


class Palindrome(Car):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        battery = SpindlerBattery(self.last_service_date)
        engine = SternmanEngine(self.warning_light_is_on)
        if battery.engine_should_be_serviced or engine.engine_should_be_serviced:
            return True
        else:
            return False
