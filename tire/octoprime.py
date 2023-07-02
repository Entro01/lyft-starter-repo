class OctoprimeTire():
    def __init__(self, arr):
        self.arr = arr
    
    def tire_should_be_serviced(self):
        if sm(self.arr) >= 3:
            return True
        else:
            return False