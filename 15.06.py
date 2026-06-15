import random
# 1
# sum = 0
# a = int(input())
# b = int(input())
# if a > b:
#     a, b = b, a
# for i in range(a,b+1):
#     sum += i
# print(sum)
# 2
# n = int(input())
# if n > 0:
#     for i in range(n, -1, -1):
#         print(i, end=" ")
# else:
#     for i in range(0, n-1, -1):
#         print(i, end=" ")
# 3
# n = int(input())
# p = 1
# for i in range(1, n+1):
#     p *= i
# print(p)
# 4
# max = int(input())
# for i in range(4):
#     a = int(input())
#     if a > max:
#         max = a
# print(max)
# 5
# sum = 0
# for i in range(5):
#     a = int(input())
#     if a // 100 != 0 and a // 1000 == 0:
#         sum += a
# print(sum)
# 6
# k = 0
# count = int(input())
# row = int(input())
# for i in range(row):
#     for j in range(count):
#         print(k, end=" ")
#         k += 1
#     print()
# 7
# column = int(input())
# row = int(input())
# for i in range(1, row+1):
#     for j in range(1, column+1):
#         k = random.randint(10,99)
#         print(k, end=" ")
#     print()
# 8
# n = int(input())
# print("* " * n)
# for i in range(n-2):
#     print("* " + "  " * (n-2) + "*")
# print("* " * n)
# 9
n = int(input())
for i in range(n):
    print(" " * (n - abs(n//2 - i)) + "*" * (abs(n//2 - i) * 2 + 1) + " " * (n - abs(n//2 - i)))



