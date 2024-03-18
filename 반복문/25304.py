x = int(input())
n = int(input())
total = 0
for i in range(n):
    price, count = map(int, input().split())
    total += price*count

if total == x:
    print('Yes')
else:
    print('No')