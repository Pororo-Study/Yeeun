a = int(input())
b = int(input())
ans = 0
for i in range(0,3):
    x = b%10
    tmp = a*x
    print(tmp)
    ans += tmp * pow(10,i)
    b = b//10

print(ans)
