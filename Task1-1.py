sum = 0
# 11 : 3, 5, 6, 9, 10
for i in range(1001):
    if i % 3 == 0 or i % 5 == 0:
        sum += i


print(sum)