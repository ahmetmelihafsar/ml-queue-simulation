import random
#from scipy.special import ndtr

class Customer:

    def __init__(self, enterTime, name, customerType, maxCustomerType, finishPos):
        self.enterTime = enterTime
        self.finishTime = None
        self.finishPos = finishPos
        self.name = name
        self.customerType = customerType

    def set_finish_time(self, time):
        self.finishTime = time

    def get_finish_pos(self):
        return self.finishPos

    def get_finish_time(self):
        return self.finishTime

    def get_enter_time(self):
        return self.enterTime

    def __str__(self):
        return "Name: {}, Enter Time: {}, Finish Time: {}, Finishing Possibility: {}, Customer Type: {}"\
        .format(self.name, self.enterTime, self.finishTime, self.finishPos, self.customerType)


