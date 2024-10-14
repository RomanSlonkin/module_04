""" KEP IT SIMPLE, STUPID  """

# def is_even(number: int) -> bool:
#     if number % 2 == 0:
#         return True
#     else:
#         return False
    
#The same as:

# def is_even(number: int) -> bool:
#     return number % 2 == 0

# print(is_even(2))
# print(is_even(15))
#################################

def is_palindrome(s: str) -> bool:
    new_s = ""
    for char in s:
        if char.isalnum():
            new_s += char.lower
    s = new_s
    length = len(s)
    for i in range(length//2):
        if s[i] != s[length-i-1]:
            return False
    return True

print(is_palindrome("Козак з казок"))