def find_average_waiting_time(allCustomers):
    totalTime = 0
    customerCount = len(allCustomers)
    for customer in allCustomers:
        totalTime += customer.get_finish_time() - customer.get_enter_time()
    return totalTime / customerCount, totalTime, customerCount


def print_average_waiting_time(allCustomers):
    avgWaitTime, totalTime, customerCount = find_average_waiting_time(allCustomers)
    print("Average Waiting Time: {}, Total Customers Served: {}, Total Waiting Time: {}".format(avgWaitTime, customerCount, totalTime))

def find_remaining_customers(queues):
    remainingCustomerCount = 0
    for queue in queues:
        remainingCustomerCount += len(queue.get_queue())
    return remainingCustomerCount


def print_remaining_customers(queues):
    print("Remaining Customer Count: {}".format(find_remaining_customers(queues)))

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # If x is greater, ignore left half
        if x < arr[mid].get_finish_pos():
            low = mid + 1

        # If x is smaller, ignore right half
        elif x > arr[mid].get_finish_pos():
            high = mid - 1

        # means x is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return low



