# def calculate_total_revenue(myServer):
#     totalWorkedTimeInMinutes = myServer.get_total_working_time()
#     totalCustomers = len(myServer.get_all_customers())
#
#     PROFIT_BY_CUSTOMER = 1.5
#     HOURLY_MINIMUM_WAGE = 22.24
#     PENALTY_FOR_EACH_REMAINING_CUSTOMER = 0.8
#
#     revenue = totalCustomers * PROFIT_BY_CUSTOMER - (totalWorkedTimeInMinutes/60 * HOURLY_MINIMUM_WAGE)\
#               - find_remaining_customers(myServer.get_queues()) * PENALTY_FOR_EACH_REMAINING_CUSTOMER
#
#     return revenue
#
# def print_revenue(myServer):
#     print("Total Revenue: {} TL".format(calculate_total_revenue(myServer)))


#self.finishPos = norm.cdf(random.uniform(0.1, 0.3)*(maxCustomerType-customerType)) # Too slow to use