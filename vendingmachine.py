'''
Implement class: VendingMachine according to the following requirements:

can be instantiated using the constructor VendingMachine(num_items, item_price)
where num_items denotes the number of items in the machine, and item_price
denotes the required number of coins to buy a single item.
has a method buy(req_items, money) that represents a buy request where req_items
denotes the requested number of items, and money is the amount the customer puts
into the machine. Depending on the state of the machine, one of the following
happens If there are enough items in the machine to serve the request and the
given money is sufficient to buy the requested number of items, the number of
items in the machine is reduced by the requested number of items. The method
returns an integer denotes the change given back after the purchase.
If there are fewer items in the machine than the requested number, it raises
a ValueError exception with the message “Not enough items in the machine”.
If there are enough items in the machine to serve the request but the given
amount of money is less than their cost, it raises a ValueError exception
with the message “Not enough coins”.
STDIN       Function
-----       --------
10 2   →    num_items = 10, item_price = 2
4      →    n = 4
1 5    →    req_items = 1, money = 5       (1st transaction)
10 100 →    req_items = 10, money = 100    (2nd transaction)
7 100  →    req_items = 7, money = 100     (3rd transaction)
2 3    →    req_items = 2, money = 3       (4th transaction)

SAMPLE OUTPUT:
3
Not enough items in the machine
86
Not enough coins

'''

import math
import os
import random
import re
import sys
class VendingMachine:
    def __init__(self,num_items,item_price):
        self.num_items=num_items
        self.item_price=item_price
    def buy(self,req_items,money):
        if req_items>self.num_items:
            return "Not enough items in the machine"
        else:
            if money>=req_items*self.item_price:
                self.num_items-=req_items
                return money-req_items*self.item_price
            else:
                return "Not enough coins"
    pass
if __name__ == '__main__':
    
    num_items, item_coins = map(int, input().split())
    machine = VendingMachine(num_items, item_coins)

    n = int(input())
    for _ in range(n):
        num_items, num_coins = map(int, input().split())
        try:
            change = machine.buy(num_items, num_coins)
            print(str(change) + "\n")
        except ValueError as e:
            print(str(e) + "\n")


    
