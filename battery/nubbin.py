from datetime import datetime

class NubbinBattery():
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date
    
    def engine_should_be_serviced(self):
        return (self.last_service_date + 4) < datetime.today().date()