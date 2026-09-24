
from functools import reduce

# # map

# lst = [2,3,4,5,6]

# lst2 = list(map(lambda x : x*x,lst))
# print(lst2)


# celsius = [0, 20, 37, 100]


# fahrenheit = list(map(lambda x :(x * 9/5) + 32,celsius))

# print(fahrenheit)


## filter 


# raw_data = ["Rahul", "", None, "Amit", 0, "Priya", False, "  "]

# clean_up= list(filter(None , raw_data))
# print(clean_up)



# ## reduce

# numbers = [47, 11, 42, 102, 13, 99]


# max_num = reduce(lambda acc, curr: acc if acc > curr else curr, numbers)

# print(max_num) 




## zip 

# keys = ["user_id", "username", "role"]
# values = [101, "rahul_dev", "admin"]


# user_dict = dict(zip(keys, values))

# print(user_dict)


# enumerator 

# menu_items = ["Home", "Profile", "Settings", "Logout"]

# for index , item in enumerate(menu_items, start = 1):
#     print(f"{index} :  {item}")


# sorted 

# users = [
#     {"name": "Rahul", "score": 85},
#     {"name": "Priya", "score": 98},
#     {"name": "Amit", "score": 72}
# ]

# high_scores =  sorted(users , key= lambda u:u["score"] , reverse=True)

# print(high_scores)


# #sum

# prices = [2,3,5]

# total = sum(prices , start = 50)

# print(total)



# any or all

latencies = [120, 85, 450, 95, 210]

check_latencies =  all(l < 500  for  l in latencies)

latencies_check = any(l < 100 for l in latencies)

print(check_latencies)
print(latencies_check)