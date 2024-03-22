n, m = map(int, input().split())
arr = [0 for _ in range(n)]
# arr = [0] * n
for _ in range(m):
    i, j, k = map(int, input().split())
    arr[i-1:j] = [k] * (j-i+1)
    # 슬라이싱한 리스트만큼을 = [k]*개수
    # for l in range(i-1, j):
    #     arr[l] = k
print(*arr)
# unpacking
# for i in arr:
#     print(i, end=' ')