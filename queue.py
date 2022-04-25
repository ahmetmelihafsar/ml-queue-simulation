from customer import Customer
import random
from free_funtions import binary_search

class Queue:

    def __init__(self, p):
        self.queue = list()
        self.newCustomerPos = p


    def get_queue(self):
        return self.queue

    def add_new_customer(self, enterTime, customerType, maxCustomerType, algorithmName):
        if random.random() <= self.newCustomerPos:
            newCustomer = Customer(enterTime, "None", customerType, maxCustomerType)
            if algorithmName == "FCFS":
                self.queue.append(newCustomer)
            elif algorithmName == "SRPT":
                index = 0
                if self.queue:
                    index = binary_search(self.queue, newCustomer.get_finish_pos())
                self.queue.insert(index, newCustomer)


    def remove_customer(self, customerIndex):
        self.queue.pop(customerIndex)

    def set_new_customer_pos(self, newP):
        self.newCustomerPos = newP

    def resetQueue(self):
        self.queue = list()
