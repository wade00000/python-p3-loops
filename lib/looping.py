#!/usr/bin/env python3

def happy_new_year():
    counter = 10
    while counter > 0:
     print(counter)
     counter -= 1
    print("Happy New Year!")

def square_integers(int_list):
   squared_list = []
   for num in int_list:
        squared_list.append(num * num)
   return squared_list

def fizzbuzz():
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)



