h, m = map(int, input().split())
# 45분 일찍 설정
if m > 45:
    m = m-45
elif m == 45:
    m = 0
else:
    if h >= 1:
        h = h - 1
    else:
        h = 23
    m = m + 60 - 45
print(f'{h} {m}')
