from typing import List
import random
from queue_random import Customer, Queue

# Longest Queue First
# This server looks at all the queues to determine which one is the longest, then it serves that queue.


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
        max_queue = self.queues[0]
        max_num = len(max_queue.queue)
        for queue in self.queues:
            if len(queue.queue) > max_num >= 0:
                max_num = len(queue.queue)
                max_queue = queue
        return max_queue
        

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