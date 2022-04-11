from typing import List
import random
from queue_random import Customer, Queue

# Template
# This file serves as a template for other algorithms. Its default function is to serve next customer in the first queue.


class Server:

    def __init__(self, name:str = "default", queues:List[Queue] = list(),next_finish_possibility=0.50, new_customer_possibility=0.40) -> None:
        if len(queues) == 0:
            queues.append(Queue(1,"q1"))
        self.name = name
        self.running = False
        self.queues = queues
        self.next_finish_possibility = next_finish_possibility 
        self.new_customer_possibility = new_customer_possibility

    
    def __get_best_queue(self) -> Queue:
        return self.queues[0]

    def run_step(self,curr_time:int):

        curr_queue = self.__get_best_queue()
        print("current time:",curr_time)
        print("length of the current queue: ", len(curr_queue.queue))
        if (len(curr_queue.queue) > 0):
            if random.random() < self.next_finish_possibility:
                curr_queue.popleft(curr_time)
        if random.random() < self.new_customer_possibility:
                new_customer = Customer(curr_time)
                curr_queue.append(new_customer,curr_time)
        print(curr_queue)
        print()