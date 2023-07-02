class CarriganTire():
    def __init__(self, arr):
        self.arr = arr
    
    def tire_should_be_serviced(self):
        if max(self.arr) >= 0.9:
            return True
        else:
            return False
            