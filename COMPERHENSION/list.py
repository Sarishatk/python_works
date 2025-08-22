arr = [6,7,8,9,10]
dict = {num:num**2 for num in arr}
print(dict)



# orders = ["tea","dosa","idli","tea",dosa]
# find {item:count}

orders = ["tea","dosa","idli","tea","dosa"]
order_counr = {items:orders.count(items) for items in orders}
print(order_counr)




# web_dict = {"one":1,"two":2,"three":3,"four":4}
web_dict = {"one":1,"two":2,"three":3,"four":4}
swap =  {v:k for k,v in web_dict.items()}
print(swap)