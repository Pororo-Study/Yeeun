h, m = map(int, input().split())
time = int(input())

m = m + time
h = h + m//60
if h>23:
    h = h-24
m = m % 60
print(f'{h} {m}')