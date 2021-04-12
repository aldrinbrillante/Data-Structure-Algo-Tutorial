

'''
HackerRank Set .add() problem
https://www.hackerrank.com/challenges/py-set-add/problem
'''

# If we want to add a single element to an existing set, we can use the .add() operation. 
# It adds the element to the set and returns 'None'.

#########################################################################################
# Apply your knowledge of the .add() operation to help your friend Rupal.

# Rupal has a huge collection of country stamps. She decided to count the total number
# of distinct country stamps in her collection. She asked for your help.
# You pick the stamps one by one from a stack of  country stamps.

# Find the total number of distinct country stamps.
#########################################################################################


#Clarify Restated question and assignment:
# Restated problem that I picked up stamps to help Rupal and
# I must find the total number of distinct country stamps


# Clarified not all stamps are countries?
# Clarified is there a possibility for repetition


# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
countries = set() #function creates a set object. The items in a set list are unordered, so it will appear in random order.
for range in range(n):
    countries.add(input())
print(len(countries))

