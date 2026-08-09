# Best time to Buy and Sell stock
# Given prices of stock on different days, find the maximum profit you can get
# You can :-> buy once, sell once

prices =[7,1,5,3,6,4]
# beginning price ->7
# profit
# min_price
# track min price and max profit for each element in list


def get_max(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        if min_price > price:
            min_price = price
        profit = price - min_price
        if max_profit < profit:
            max_profit = profit
        # print(price, min_price,max_profit)

    return max_profit

profit = get_max(prices)
# print(f"Maximum profit we can get: {profit}")

##################################################################################################################

# parsing logs

logs = [
    "2024-01-01T10:15:30 INFO user1 login",
    "2024-01-01T11:00:00 ERROR user2 failed",
    "2024-01-01T12:30:00 ERROR user2 timeout",
    "2024-01-01T12:15:30 ERROR user1 timeout",
    "2024-01-02T09:00:00 ERROR user1 failed",
    "2024-01-02T10:00:00 ERROR user1 crash",
    "2024-01-02T11:00:00 INFO user2 success"
]

# output:
# {'2024-021-01': {'user2':2,'user1':1}, '2024-01-02': {'user1':2}}

def error_log(logs):
    result={}

    for log in logs:

        log_date = log.split()[0][0:10]
        msg = log.split()[1]
        user = log.split()[2]

        if msg == 'ERROR':
            if log_date not in result:
                result[log_date] = {}

            result[log_date][user] = result[log_date].get(user,0)+1
    return result
        # print(log_date, msg, user)

print(f"log summary: {error_log(logs)}")