from car import Car


class Glissade(Car):
    def __init__(self, last_service_date, current_mileage, last_service_mileage, tire_type, sensor_array):
        super().__init__(last_service_date)
        self.tire_type = tire_type
        self.sensor_array = sensor_array        
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        battery = SpindlerBattery(self.last_service_date)
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        if self.tire_type == 'Carrigan':
            tire = CarriganTire(sensor_array)
        else:
            tire = OctoprimeTire(sensor_array)
        if battery.engine_should_be_serviced or engine.engine_should_be_serviced or tire.tire_should_be_serviced:
            return True
        else:
            return False
