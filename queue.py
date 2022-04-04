#  Author: Ahmet Melih Afsar

import random
from typing import List




stepping = 1

class Queue:
    def __init__(self,name:str = "default",customer_num:int = 2) -> None:
        self.name = name
        self.customer_num = customer_num

    def __str__(self) -> str:
        return f"Queue: {self.name}, customers={self.customer_num} "
        


class Server:
    def __init__(self, name:str = "default", queues:List[Queue] = list()) -> None:
        if len(queues) == 0:
            queues.append(Queue("q1",1))
        self.name = name
        self.running = False
        self.last_step_run = 0
        self.queues = queues
        self.processing_time = 15
        self.curr_queue = None
        self.finished_percent = 0
    
    def __run(self):
        print("im running")


    def __get_from_queue(self) -> bool:
            max_queue = self.queues[0]
            max_num = max_queue.customer_num
            for queue in self.queues:
                if queue.customer_num > max_num >= 0:
                    max_num = queue.customer_num
                    max_queue = queue
            if max_num > 0:
                max_queue.customer_num -= 1
                self.curr_queue = max_queue
                return True
            else:
                return False




    def run_step(self,curr_step:int):
        if (max(queue.customer_num for queue in self.queues) > 0):
            if self.running == False:
                if self.__get_from_queue():
                    self.running = True
                    self.last_step_run = curr_step
                    return
                else:
                    # print("queues are empty!")
                    return "empty"
                
        else:
            print("queues are empty!")
            self.running = False
            return "empty"

        self.finished_percent = (curr_step - self.last_step_run) * 100 / self.processing_time 
        if (curr_step - self.last_step_run) >= self.processing_time and self.running:
            self.__run()
            self.last_step_run = curr_step
            self.running = False
            self.finished_percent = 100


q1,q2 = Queue("q1",2 ), Queue("q2", 3)
queues = [q1,q2]
ser = Server("myServer", queues)

for step in range(10):
    print(step)
    if ser.run_step(step) == "empty":
        continue
    print(f"server: {ser.name} | queue: {ser.curr_queue.name} | done: %{ser.finished_percent:.2f}")
    print(q1, q2)
    if random.random() < 0.15:
        q1.customer_num += 1
    
