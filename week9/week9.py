# def is_odd(n):
#     return n % 2 == 1
# print(is_odd(5))
from unittest import result


# def is_leayear(year):
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True
#     else:
#         return False
#
# print(is_leayear(2024))


# def print_triangular_numbers(n):
#     total = 0
#     for i in range(1, n+1):
#         total = total + i
#         print(i, total)
#
# print_triangular_numbers(5)

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# print(is_prime(2))

# def reverse(s):
#     result = ""
#     for ch in s:
#         result = result + ch
#     return result
#
# print(reverse("abcd"))
#
# def reverse_slice(s):
#     return s[::-1]
# print(reverse_slice("abcd"))


# def remove_all(sub, s):
#    return s.replace(sub, "*")
# print(remove_all("l", "hello world"))


# def substitute(message, key):
#     alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
#     result = ""
#     for ch in message:
#         index = alphabet.find(ch.lower())
#         if index == -1:
#             result = result + ch
#         elif ch.isupper():
#             result = result + key[index].upper()
#         else:
#             result = result + key[index].lower()
#     return result
#
# key = "qtgqwertyuıopğüasdfghjklşizxc"
# print(len(key))
# print(substitute("Hello, World!", key))

# def remove_dups(s):
#     result = ""
#     for ch in s:
#         if ch not in result:
#             result += ch
#     return result
#
# print(remove_dups("hello world"))