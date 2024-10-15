""" DON'T REPEAT YOURSELF"""


# # Розрахунок площі 
# length1, width1 = 5, 10
# area1 = length1 * width1

# # Багато різного коду

# length2, width2 = 7, 12
# area2 = length2 * width2

"""Щоб застосувати принцип DRY нам потрібно повторюваний код помістити в функцію: """

# def calculate_area(length: float, width: float) -> float:
#     return length * width

# area1 = calculate_area(5, 10)
# area2 = calculate_area(7, 12)


