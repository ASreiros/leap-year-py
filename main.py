year = int(input("Which year do you want to check? "))

flag = False

if year % 400 == 0:
    flag = True
elif year % 4 == 0:
    if year % 100 != 0:
        flag = True


if flag == True:
    print("Leap year.")
else:
    print("Not leap year.")
