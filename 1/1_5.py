#coding:utf-8
# start=0
# sum=0
# while True:
#     start+=1
#     if start==100:
#         break
#     elif start%2!=0:
#         sum=sum+start
#     elif start%2==0:
#         sum=sum-start
#     else:
#         pass
# print sum

#_*_ coding:utf-8 _*_
sum1 = 0
sum2 = 0
for i in range(1,100):
    if i%2 != 0:
        sum1 = sum1 + i
    else:
        sum2 = sum2 + i
sum = sum1-sum2
print(sum)


