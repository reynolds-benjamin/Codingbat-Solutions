#Q1
#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
#We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
    return (not weekday or vacation)

#Q2
#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling.
# We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

#Q3
#Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b
    
#Q4
#Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

def diff21(n):
  if n > 21:
    return 2 * (n - 21)
  else:
    return 21 - n
  
#Q5
#We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. 
#We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

#Q6
#Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

def makes10(a, b):
    if a + b == 10 or (a == 10 or b == 10):
        return True
    else:
        return False
    
#Q7
#Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
    return ((110 >= n >= 90) or (210 >= n >= 190)) 
