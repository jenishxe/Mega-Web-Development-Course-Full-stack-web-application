################################## python Advance #########################################

# class Order:
#     def __init__(self, username, total, membership):
#         self.username = username
#         self.total = total
#         self.is_membership = membership

     






'''
# profit margin = net-income/revenue x 100
revenue = int(input("How much is your monthly revenue: "))
expense = int(input("How much is your monthly expense: "))

def cal_margin(made, expense):
    net_income = made - expense
    return (net_income/made)*100

print(f"Your profit margin: {cal_margin(revenue, expense)}")

'''




################################## python intermediate #########################################


"""
Password genserator 
length of the password

lowercase
uppercase
numbers
symbol

import string, random

length = int(input("Enter the lenght of the password: \n"))


lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbol = string.punctuation

all = lower + upper + num + symbol

sample = random.sample(all, length)
password = "".join(sample)
print(password)

"""










# append even numbers to the list
'''
even_numbers = []
while True:
    y = input("Do you want to add Number again? ('y' for Yes  or 'n' for No): ").lower()
    if y == 'y':
        try:
            a = int(input("Enter a Number: "))
            if a % 2 ==0:
                even_numbers.append(a)
            else:
                print(f"{a} is not a even number") 
        except ValueError:
            print("Please enter a valid Integer")
            
    elif y== 'n':
        if even_numbers:
            print(f"Even numbers are: {even_numbers}")
        else:
            print(f"No Even numbers entered : {even_numbers}")
        break
    else:
        print("Invalid Input")

'''

# odd_num = []
# even_num = []
# for i in range(1,101):
#     if i % 2 == 0:
#         even_num.append(i)
#     else:
#         odd_num.append(i)

# print(odd_num)
# print(even_num)




################################## python beginner #########################################
# https://thonny.org/

# name = input("Enter your name:- \n \n")
# age = int(input("Enter your Age:- \n"))

# print(f"Hello i'm {name} and im {age} years old")


# break even point 

# fixed cost / saler per unit - cost per unit
#Eg imagine ayou renterd a shop for 2500 per month Each costs 1.4 to 2.95
'''
rent = 2500
coffee_price = 2.95
coffee_costs = 1.4

break_even = rent/(coffee_price-coffee_costs)

print(f"Your break even point is {break_even}")
'''


'''
#A shop will give a discount of 5% if the purchased amount is over $200 and 15% if the purchse is over $500


quantity = int(input("how many product will you order"))

cost = quantity * 50
membership ="vip"

if cost >= 500 or membership == "vip":
    discount = (cost/100)*15
    print(f"The cost is ${cost} and Discount {discount}")
    print(f"You need to pay {cost - discount}")
elif cost >= 200:
    discount = (cost/100)*5
    print(f"The cost is ${cost} and Discount {discount}")
    print(f"You need to pay {cost - discount}")
else:
    print(f"The cost is {cost}. Order more products for discounts.")

'''