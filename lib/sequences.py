#!/usr/bin/env python3

def print_fibonacci(length):
    fib_list = [0,1]
    if length == 0:
        print([])
    elif length < 3:
        print(fib_list[0:length])
    else:
        for n in range(length - 2):
            next_num = fib_list[-2] + fib_list[-1]
            fib_list.append(next_num)
        print (fib_list)
