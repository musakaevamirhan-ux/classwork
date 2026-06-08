# 1
# a = int(input())
# b = int(input())
# c = int(input())
# if a > b and a > c:
#     print(a)
# elif b > c and b > a:
#     print(b)
# else:
#     print(c)
# 2
# a = int(input())
# if a % 2 == 0:
#     print("YES")
# else:
#     print("NO")
# 3
# a = int(input())
# if a % 10 == 3 or a // 10 == 3:
#     print("YES")
# else:
#     print("NO")
# 4
# a = int(input())
# if 10 <= a <= 20:
#     print("YES")
# else:
#     print("NO")
# 5
# a = int(input())
# b = int(input())
# if a % 3 == 0 and b % 3 == 0:
#     print("YES")
# else:
#     print("NO")
# n = int(input())
# while n > 0:
#     print("Hello")
#     n -= 1
# k = int(input())
# while k >= 0:
#     print(k, end=" ")
#     k -= 1
# n = int(input())
# a = 0
# while a <= n:
#     print(a, end=" ")
#     a += 1
# a = int(input())
# b = int(input())
# if b >= a:
#     a, b = b, a
# while a>=b:
#     print(a, end=" ")
#     a -= 1
# a = int(input())
# b = int(input())
# if a >= b:
#     a, b = b, a
# if a%2 == 1:
#     a += 1
# while a <= b:
#     print(a, end=" ")
#     a += 2
# n = int(input())
# a = 3
# while a <= abs(n):
#     if n > 0:
#         print(a, end=" ")
#     else: print(-a, end=" ")
#     a += 10
k = 0
summ = 0
while True:
    a = int(input())
    if a == 0:
        break
    summ += a
    k += 1
print(summ/k)

