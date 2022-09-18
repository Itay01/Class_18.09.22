# Assignment 1:
list = [num for num in range (1000, 10000) if ((num % 100 + num // 100)**2) == num]
print(list)

# Assignment 2:
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

# Assignment 3:
num = int(input("enter first number: "))
for i in range(1, num + 1):
    s = ''
    for j in range(i, 0, -1):
        s += str(j) + ' '
    print(s)

for i in range(num-1, 0, -1):
    s = ''
    for j in range(i, 0, -1):
        s += str(j) + ' '
    print(s)

# # Assignment 4:
for num in range(0, 6):
    for num_add in range(1, 11):
        number = num + num_add/10
        if number % 1 == 0:
            print(int(number))
        else:
            print(number)
