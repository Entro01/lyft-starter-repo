from car import Car


class Rorschach(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        battery = NubbinBattery(self.last_service_date)
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        if battery.engine_should_be_serviced or engine.engine_should_be_serviced:
            return True
        else:
            return False
