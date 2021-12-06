""" Simple addition function"""

num1 = int(input("Enter First Num: "))
num2 = int(input("Enter Second Num: "))
print( int(num1) + int(num2));

"""Simple For Loops"""
for index in range(5):
    print(index)

lucky_nums = [4, 8, 15, 16, 23, 42]
for lucky_num in lucky_nums:
    print(lucky_num)

for letter in "Giraffe":
    print(letter)

"""Exponent Function"""

def raise_to_power(base_num, pow_num):
     result = 1
     for index in range(pow_num):
          result *= base_num
     return result