#  using arrays for storing stock prices:

# import os
# print(os.getcwd())

stock_prices = []
with open("stock_prices.csv","r") as f:
    print("Opening....")
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices.append([day,price])
    print("Closing...")

print(stock_prices,"\n\n")
print(stock_prices[0])


# Stock price on March 9:
for elem in stock_prices:
    if elem[0] == "march 9":
        print(elem[1])
# Complexity of search using a list is O(n)


# PROCESS using PYTHON DICTIONARY:

stock_prices = {}
with open("stock_prices.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price

print("\n",stock_prices,"\n\n")

print(stock_prices["march 9"])


"""++++++++++++++++++++++++ IMPLEMENTING HASH TABLE +++++++++++++++++++++++++"""
def get_hash(key):
    hash_value = 0
    for char in key:
        hash_value += ord(char)
    print(hash_value % 100)

get_hash("march 6")

# creating a Hastable:

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for _ in range(self.MAX)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX

    def __getitem__(self,index):
        h = self.get_hash(index)
        return self.arr[h]

    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


t = HashTable()
t["march 6"] = 310
t["march 7"] = 420

print(t["march 6"])
print(t.arr)

t["dec 30"] = 88

print("\n\n",t["march 7"],t["dec 30"])