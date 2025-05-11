#!/usr/bin/env python3

def happy_new_year():
    count = 10
    while count > 0:
        print(count)
        count -=1
        print("Happy New Year!")
    pass

def square_integers(int_list):
    return [ x **2 for x in int_list] 
    pass

def fizzbuzz():
    for number in range(1, 101):  
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

