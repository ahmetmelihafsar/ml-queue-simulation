from typing import List
import random
from queue_random import Customer, Queue

# First Come First Serve Algorithm
# This server looks at the next customers of all the queues. Selects the queue with the customer that entered earliest and run its job. 

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
        times_of_end_customers = list()
        queue_to_return = self.queues[0]
        try:
            for queue_of_loop in self.queues:
                current_customer:Customer = queue_of_loop.queue[0]
                times_of_end_customers.append(current_customer.enter_time)
            time_of_earliest_customer = min(times_of_end_customers)
            for queue_of_loop in self.queues:
                current_customer:Customer = queue_of_loop.queue[0]
                if current_customer.enter_time == time_of_earliest_customer:
                    queue_to_return = queue_of_loop
        except IndexError: # when queue is empty, queue.queue[0] can raise IndexError, but unless all queues are empty it is fine. The case where all queues are empty is also taken care of.
            pass
        return queue_to_return

    def run_step(self,curr_time:int):

        curr_queue = self.__get_best_queue()
        # print("current time:",curr_time)
        # print("length of the current queue: ", len(curr_queue.queue))
        if (len(curr_queue.queue) > 0):
            if random.random() < self.next_finish_possibility:
                curr_queue.popleft(curr_time)
        if random.random() < self.new_customer_possibility:
                new_customer = Customer(curr_time)
                curr_queue.append(new_customer,curr_time)
        # print(curr_queue)
        # print()
