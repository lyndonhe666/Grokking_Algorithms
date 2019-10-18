# 阶乘
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
a = factorial(5)
print(a)

# Leetcode No.17:Letter combination of a phone number
# Problem description:
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# example :
# input:'23'
# output:["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
def lettercombination(s):
    

