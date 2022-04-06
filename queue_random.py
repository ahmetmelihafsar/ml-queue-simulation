#  Author: Ahmet Melih Afsar

import random
from typing import List
from collections import deque

init_time = 0

class Customer:
    all_customers = list()
    def __init__(self, arrival_time:int=init_time,name:str="") -> None:
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
        return f"Customer: {self.name}, enter_time: {self.enter_time}, leave_time: {self.leave_time} "
    


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



class Server:
    def __init__(self, name:str = "default", queues:List[Queue] = list()) -> None:
        if len(queues) == 0:
            queues.append(Queue(1,"q1"))
        self.name = name
        self.running = False
        self.queues = queues

    
    def __get_best_queue(self) -> Queue:
        return self.queues[0]

    def run_step(self,curr_time:int):
        next_finish_possibility = 0.50
        new_customer_possibility = 0.40

        curr_queue = self.__get_best_queue()
        # for i in self.queues:
        #     print(i)
        print("len: ", len(curr_queue.queue))
        # if (max(len(queue.queue) for queue in self.queues) > 0):
        if (len(curr_queue.queue) > 0):
            if random.random() < next_finish_possibility:
                curr_queue.popleft(curr_time)
        if random.random() < new_customer_possibility:
                new_customer = Customer(curr_time)
                curr_queue.append(new_customer,curr_time)
        print(curr_queue)




def print_all_customers():
    for x in Customer.all_customers:
        print(x)
        


def main():
    time_length = 100
    q1,q2 = Queue(2,"q1"), Queue(3,"q2")
    queues = [q1,q2]
    ser = Server("myServer", queues)

    for time in range(time_length):
        ser.run_step(time)


if __name__ == "__main__":
    main()


print_all_customers()