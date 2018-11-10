# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 15:01:51 2018

@author: 11270
"""

"""
Problem 1

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', 
your program should print:

Number of vowels: 5
"""

s = input('write a string: ')
vowels = 0

for n in range(len(s)):
    if s[n] in ['a', 'e', 'i', 'o', 'u']:
        vowels += 1
        
print("Number of vowels: " + str(vowels))



"""
Problem 2

Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

s = input('write a string: ')
bob = 0

for n in range(len(s) - 2):
    if s[n:n + 3] == 'bob':
        bob += 1
        
print("Number of times bob occurs is: " + str(bob))


"""
Problem 3
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters 
occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your 
program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', 
then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. If you've 
spent more than a few hours on this problem, we suggest that you move on to a 
different part of the course. If you have time, come back to this problem after 
you've had a break and cleared your head.
"""


s = input('write a string: ')
length = len(s)
maxsofar = s[0]
current = s[0]

for n in range(1,length):
    for i in range(n,length):
        if s[i - 1] > s[i]:
            break
        else:
            current += s[i]
    if len(current) > len(maxsofar):
        maxsofar = current
    current = s[n]
        
print("Longest substring in alphabetical order is: " + maxsofar)

