from datetime import datetime

class SpindlerBattery():
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
    
    def engine_should_be_serviced(self):
        return (self.last_service_date + 3) < datetime.today().date()
