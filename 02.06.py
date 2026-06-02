a = int(input())
t = a%10
r = a//1000
k = (a%1000)//100
g = (a%100)//10
print(t*1000 + g*100 + k*10 + r)