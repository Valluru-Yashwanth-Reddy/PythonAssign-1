# Easy-1

def calculate_average(numbers):
    return sum(numbers)/len(numbers) if numbers else 0
print(calculate_average([5,10,15,20]))
print(calculate_average([]))

# Easy-2

def greet_user(name, greeting="Hello"):
    return f"{greeting}, {name} !"
print(greet_user("Alice")) 
print(greet_user("Bob", "Hi")) 


# Medium -1 

def calculate_total(*prices, discount=0):
    total = sum(prices)
    discount_amt = total * discount /100
    return total - discount_amt
print(calculate_total(10, 20, 30))
print(calculate_total(10, 20, 30, discount=10))


# Medium - 2

def create_multiplier(n):
    return lambda x: x*n
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))  
print(triple(5))  