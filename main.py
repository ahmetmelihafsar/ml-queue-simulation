from queue import Queue
from server import Server
from free_funtions import *

LOOP_COUNT = 1000000
DEFAULT_PROBABILITY = 0.5
INCREASED_PROBABILITY = 0.7

myQueue = Queue(p=DEFAULT_PROBABILITY)
myQueue2 = Queue(p=DEFAULT_PROBABILITY)
allQueues = [myQueue, myQueue2]

# Possible Algorithm Names: "SRPT", "FCFS"
myServer = Server(allQueues, serverCount=3, algorithm_name="SRPT")


for time in range(1, LOOP_COUNT + 1):
    myServer.iterate_server(time)
    if time % 10000 == 0:
        print(time)
    # Assume loop starts at 00.00 and goes until 23.59.59
    # When 1/3 of the day is passed, it means time is 08.00
    # At that time possibility of a customer to arrive is increased
    # Until 2/3 of the day which is 16.00
    if time == LOOP_COUNT // 3:
        myServer.set_all_new_customer_pos(INCREASED_PROBABILITY)
    if time == LOOP_COUNT // 3 * 2:
        myServer.set_all_new_customer_pos(DEFAULT_PROBABILITY)

print("*******************")
print("Statistics: ")
print_average_waiting_time(myServer.get_all_customers())
print_remaining_customers(myServer.get_queues())
print("*******************")

