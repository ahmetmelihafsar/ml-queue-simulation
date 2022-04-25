import random
import sys


class Server:

    def __init__(self, queues, serverCount, algorithm_name):
        self.queues = queues
        self.allCustomers = list()
        self.serverCount = serverCount
        self.workingTimeInUnitTime = 0
        self.candidateFinder = self.return_function_to_find_best_candidate(algorithm_name)
        self.algorithmName = algorithm_name

    def get_queues(self):
        return self.queues

    def get_all_customers(self):
        return self.allCustomers

    def get_total_working_time(self):
        return self.workingTimeInUnitTime

    def set_all_new_customer_pos(self, p):
        for queue in self.queues:
            queue.set_new_customer_pos(p)

    def reset_queues(self):
        for queue in self.queues:
            queue.resetQueue()

    def reset_working_time(self):
        self.workingTimeInUnitTime = 0

    def reset_all_customers(self):
        self.allCustomers = list()

    def return_function_to_find_best_candidate(self, algorithm_name):
        if algorithm_name == "SRPT":
            return self.find_best_candidate_for_SRPT
        if algorithm_name == "FCFS":
            return self.find_best_candidate_for_FCFS

    def add_customer_to_all_queues(self, time):
        # Adds new customers to the queues based on current time and customer-types
        # Customer types are equal to index number of the queues
        customerType = 1
        MAX_CUSTOMER_TYPE_COUNT = len(self.queues) + 1
        #####################################################################################
        # Following can be used to make customer type not dependend on index number of queues
        # MAX_CUSTOMER_TYPE_COUNT = 2
        # customerType = random.randint(1,MAX_CUSTOMER_TYPE_COUNT)
        #####################################################################################
        for queue in self.queues:
            queue.add_new_customer(time, customerType, MAX_CUSTOMER_TYPE_COUNT, self.algorithmName)
            customerType += 1

    def find_best_candidate_for_FCFS(self):

        bestQueue = self.queues[0]
        minEnterTime = sys.maxsize

        for queue_obj in self.queues:
            # Check if the current queue is empty or not
            # Get the list in the queue object
            queue = queue_obj.get_queue()
            if queue:
                # Get the first element of the current queue
                # Only first element will be checked because newcomers added to the end
                # Therefore in each queue, elements which has been waiting at most
                # Will be at the beginning of the queue
                customer = queue[0]
                customerEnterTime = customer.get_enter_time()

                # If current customer is waiting more than previous one, make it best customer to iterate
                if customerEnterTime < minEnterTime:
                    minEnterTime = customerEnterTime
                    bestQueue = queue_obj

        return (bestQueue, 0)


    def find_best_candidate_for_SRPT(self):
        bestQueue = self.queues[0]
        maxPossibility = 0

        for queue_obj in self.queues:
            # Get the list in the queue object
            queue = queue_obj.get_queue()
            if queue:
                # Get the customer at the customer index in the current queue
                customer = queue[0]
                # If current customer is more likely to end compared to previous one
                # Make current customer the best customer to iterate
                if customer.get_finish_pos() > maxPossibility:
                    maxPossibility = customer.get_finish_pos()
                    bestQueue = queue_obj

        return (bestQueue, 0)


    def iterate_server(self, time):
        # Get the function to find the best candidate based on the given algorithm
        candidate_finder = self.candidateFinder

        # Increase total working time
        self.workingTimeInUnitTime += self.serverCount

        # Run the algoritm as many as server count
        for i in range(self.serverCount):
            # Get the best candidate for iterate
            currQueue, currCustomerIndex = candidate_finder()

            # Check if the queue is empty
            if currQueue.get_queue():
                # If the current queue is not empty, then iterate the system
                self.iterate_queue(currQueue, currCustomerIndex, time)

        # Add new customer for every queue
        self.add_customer_to_all_queues(time)


    def iterate_queue(self, currQueue, bestCustomerIndex, time):
        ##############################################
        # This block is added to test the algorithms
        # print("*****************")
        # queueNum = 1
        # for queue in self.queues:
        #     print("Queue Number: {}".format(queueNum))
        #     for customer in queue.get_queue():
        #         print(customer)
        #     queueNum += 1
        # print("******************")
        ###############################################
        queue = currQueue.get_queue()
        bestCustomer = queue[bestCustomerIndex]
        if random.random() <= bestCustomer.get_finish_pos():
            currQueue.remove_customer(bestCustomerIndex)
            bestCustomer.set_finish_time(time)
            self.allCustomers.append(bestCustomer)

            ####################################################
            # This block is added to test the algorithms
            # print("-----------------")
            # print("Popped Customer: {}".format(bestCustomer))
            # print("------------------")
            ####################################################

