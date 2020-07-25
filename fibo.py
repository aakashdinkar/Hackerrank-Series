inp = int(input())
count = 0
lst = []
n1, n2 = 0, 1
lst.append(n1)
lst.append(n2)
while count < inp:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    lst.append(n3)
    # print(n3)
    count += 1
sum_fib = 0
for i in range(len(lst)):
    if i % 2 == 0:
        sum_fib += lst[i]

print(sum_fib)