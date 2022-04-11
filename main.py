from queue_random import Customer, Queue
# from algorithms.template import Server
from algorithms.fcfs import Server


def print_all_customers():
    time_waited_sum = 0
    customer_num = 0
    x:Customer
    for x in Customer.all_customers:
        # print(x)
        if type(x.leave_time) == int and type(x.enter_time) == int: 
            if x.leave_time == 0:
                continue
            time_waited_sum += x.leave_time - x.enter_time 
            customer_num += 1
    average_wait_time = time_waited_sum / customer_num
    print(f"{customer_num=} {time_waited_sum=} {average_wait_time=:.2f}")

def main():
    time_length = 1000000
    q1 = Queue(2,"q1")
    queues = [q1,]
    ser = Server("myServer", queues)
    for time in range(time_length):
        ser.run_step(time)

    print_all_customers()


if __name__ == "__main__":
    main()