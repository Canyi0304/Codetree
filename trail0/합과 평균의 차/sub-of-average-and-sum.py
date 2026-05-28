a,b,c = map(int, input().split())
sum = a + b + c
average = int((a + b + c) / 3)
sum_minus_average = int(sum - average)
print(sum)
print(average)
print(sum_minus_average)