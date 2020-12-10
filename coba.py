#!bin/python3
# z = ""
# name = list('Helen')
# for x in range(len(name)):
#     y = name[x]
#     z += y
#
# print(z)
# angka = 0
#
# while angka < 100:
#     if angka % 3 == 0:
#         print(angka)
#     angka += 1

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


#
# if __name__ == '__main__':
#     n = int(input().strip())
#
#     if n % 2 == 0 and (n in range(2, 6) or n > 20):
#         print('Not Weird')
#     else:
#         print('Weird')


# n = int(input())
#
# for x in range(0, n):
#     y = x ** 2
#     print(y)

# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#         if year % 4 == 0:
#         if year % 100 != 0:
#             leap = True
#         elif year % 400 == 0:
#             leap = True
#
#     return leap
#
# year = int(input())
# print(is_leap(year))

# n = int(input())
# string1 = ""
#
# for x in range(1, n+1):
#     string1 += str(x)
#
# print(string1)

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    mean = 0
    if query_name in student_marks:
        for i in student_marks[query_name]:
            mean += i
        count = mean / len(student_marks[query_name])
        print(f'{count:.2f}')
