# while(True):
#     try:
#         a, b = map(int(input().split()))
#         print(a+b)
#     except:
#         break

import sys
input = sys.stdin.readlines()

for i in input:
    a, b = map(int, i.split())
    print(a+b)
