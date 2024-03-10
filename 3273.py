n = int(input())
arr = list(map(int, input().split()))
x = int(input())

# 정렬
arr.sort()

count = 0
left = 0 # 시작
right = n-1 # 끝
while left < right:
    if arr[left] + arr[right] == x:
        count += 1
        left += 1
    elif arr[left] + arr[right] > x:
        right -= 1
    else:
        left += 1

print(count)