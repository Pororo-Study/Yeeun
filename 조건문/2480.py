abc = list(map(int, input().split()))

abc.sort()
if (abc[0] == abc[1]) and (abc[1] == abc[2]):
    print(10000 + (abc[0]*1000))
elif (abc[0] != abc[1]) and (abc[1] == abc[2]):
        print(1000 + abc[1]*100)
elif (abc[0] == abc[1]) and (abc[1] != abc[2]):
        print(1000 + abc[0]*100)  
else:
    print(abc[2]*100)

# a,b,c = map(int, input().split())

# if a==b==c:
#     print(10000+a*1000)
# elif a==b:
#     print(1000+a*100)
# elif b==c:
#     print(1000+b*100)
# elif c==a:
#     print(1000+c*100)
# else:
#     print(max(a,b,c)*100)