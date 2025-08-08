class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType):
        if carType == 1:
            if self.big - 1 >= 0:
                self.big -= 1
                return True
        if carType == 2:
            if self.medium - 1 >= 0:
                self.medium -= 1
                return True
        if carType == 3:
            if self.small - 1 >= 0:
                self.small -= 1
                return True
        return False


# Your ParkingSystem object will be instantiated and called as such:
obj = ParkingSystem(1, 1, 0)
param_1 = obj.addCar(1)
print(param_1)