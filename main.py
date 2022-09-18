list = [num for num in range (1000, 10000) if ((num % 100 + num // 100)**2) == num]
print(list)

number = int(input("Enter a number: "))
list_number = [int(num) for num in str(number)]
odd = 0
even = 0

for num in list_number:
    if num % 2 == 0:
        even += num
    else:
        odd += num

if odd == even:
    print("True")
else:
    print("False")

num = int(input("enter first number: "))
x = 1
for i in range(1, num + 1):
    s = ''
    for j in range(i, 0, -1):
        s += str(j) + ' '
    print(s)
