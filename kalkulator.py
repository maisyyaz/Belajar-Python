# a = int(input())
# b = int(input())
# c = int(input())
# print((a + b + c) // 2 + (a + b + c) % 2)

# anne true
# average_grade = 49
# recommended_by_tutor = True
# finished_introductory_course = False
# introductory_course_grade = 0
# enroll_student = ((average_grade >= 40 and recommended_by_tutor) or (finished_introductory_course and introductory_course_grade > 85))
# print(enroll_student)

# john false
# average_grade = 41
# recommended_by_tutor = False
# finished_introductory_course = True
# introductory_course_grade = 76
# enroll_student = ((average_grade >= 40 and recommended_by_tutor) or (finished_introductory_course and introductory_course_grade > 85))
# print(enroll_student)

# Frank true
# average_grade = 37
# recommended_by_tutor = True
# finished_introductory_course = True
# introductory_course_grade = 97
# enroll_student = ((average_grade >= 40 and recommended_by_tutor) or (finished_introductory_course and introductory_course_grade > 85))
# print(enroll_student)

# victoria true
# average_grade = 40
# recommended_by_tutor = True
# finished_introductory_course = True
# introductory_course_grade = 86
# enroll_student = ((average_grade >= 40 and recommended_by_tutor) or (finished_introductory_course and introductory_course_grade > 85))
# print(enroll_student)

# mary false
# average_grade = 49
# recommended_by_tutor = False
# finished_introductory_course = True
# introductory_course_grade = 85
# enroll_student = ((average_grade >= 40 and recommended_by_tutor) or (finished_introductory_course and introductory_course_grade > 85))
# print(enroll_student)

# sam false
# average_grade = 33
# recommended_by_tutor = False
# finished_introductory_course = True
# introductory_course_grade = 51
# enroll_student = ((average_grade >= 40 and recommended_by_tutor) or (finished_introductory_course and introductory_course_grade > 85))
# print(enroll_student)

# height = 10
# width = 35
# length = 35
# allowed = (height <= 10 < width <= 35 < length <= 40) or (height + width + length <= 80)
# print(allowed)

# a = int(input())
# b = int(input())
# c = int(input())

# print(((a / b) % 2) == 1)
# hasil = c // a
# print(hasil)

# harvard = "linguistics, physics, programming, fine arts"
# stanford = "biology, classics, geophysics, music"
#
# arts = "linguistics, fine arts, classics, music"
# sciences = "physics, programming, biology, geophysics"
#
# major = "biology"
# if major in harvard:
#     if major in arts:
#         print("This is an arts program at Harvard")
#     if major in sciences:
#         print("This is a sciences program at Harvard")
# if major in stanford:
#     if major in arts:
#         print("This is an arts program at Stanford")
#     if major in sciences:
#         print("This is a sciences program at Stanford")

# sound = "music"
# n_people = 11
# if sound == "music" and n_people > 10:
#     print("We are at the party!")

# pasta = "tomato, basil, garlic, salt, pasta, olive oil"
# apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
# ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
# chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
# omelette = "egg, milk, bacon, tomato, salt, pepper"
#
# a = input()
# if a in pasta:
#     print("pasta time!")
# if a in apple_pie:
#     print("apple pie time!")
# if a in ratatouille:
#     print("ratatouile time!")
# if a in chocolate_cake:
#     print("chocolate cake time!")
# if a in omelette:
#     print("omelete time!")

# number = int(input())
# word = input()

# write a condition for plurals
# if number > 1:
#     word = word + "s"
#
# print(number, word)

# x = 25
# while x % 2 != 0:
#     print(x)
#     x += 3

# number = 0
# while number < 12:
#     print(number)
#     number += 2

# n = int(input())
# num = 1
#
# while n >= 1:
#     num = num * n
#     n = n - 1
# print(num)

# initial = int(input())
# final = int(input())
# days = 0
# h_life = 12
#
# while initial >= final:
#     initial //= 2
#     days += h_life
#
# print(days)

a = int(input())
b = 0

while b < a - 2:
    b += 2
    print(b)

