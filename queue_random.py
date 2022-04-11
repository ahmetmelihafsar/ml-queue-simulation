#  Author: Ahmet Melih Afsar

import random
from typing import List
from collections import deque

init_time = 0

class Customer:
    all_customers = list()
    def __init__(self,name:str="") -> None:
        self.name = name
        self.leave_time = -1
        self.all_customers.append(self)
    
    def leave(self, curr_time):
        self.leave_time = curr_time
    
    def enter(self, curr_time):
        self.enter_time = curr_time

    def __str__(self) -> str:
        if self.leave_time == -1:
            self.leave_time = "not left"
        return f"Customer: {self.name},\tenter_time: {self.enter_time},\tleave_time: {self.leave_time} "
    


class Queue:
    def __init__(self, initial_customer_num:int=10, name:str="default") -> None:
        self.queue = deque()
        self.name = name
        for i in range(initial_customer_num):
            self.append(Customer(), init_time)
    

    def popleft(self, curr_time):
        x:Customer = self.queue.popleft()
        x.leave(curr_time)
    
    def pop(self, curr_time):
        x:Customer = self.queue.pop()
        x.leave(curr_time)

    def append(self, customer:Customer, curr_time):
        x = self.queue.append(customer)
        customer.enter(curr_time)

    def appendleft(self, customer:Customer, curr_time):
        x = self.queue.appendleft(customer)
        customer.enter(curr_time)
    
    def __str__(self) -> str:
        temp = f"Queue: {self.name}"
        for customer in self.queue:
            temp += f"\n{customer}"
        return temp
