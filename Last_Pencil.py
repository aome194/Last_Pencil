import random

print("How many pencils would you like to use:")
pencils_number_string = input()
i = 1

while i == 1:
    if pencils_number_string.isdigit() == False:
        print("The number of pencils should be numeric")
        i = 1
        pencils_number_string = input()
    else:
        if pencils_number_string == '0':
            print("The number of pencils should be positive")
            i = 1
            pencils_number_string = input()
        elif int(pencils_number_string) < 0:
            print("The number of pencils should be numeric")
            i = 1
            pencils_number_string = input()
        else:
            pencils_number = int(pencils_number_string)
            print("Who will be the first (John, Jack):")
            i = 0

name_first = input()
good_name_list = ["John", "Jack"]
good_number_list = ['1', '2', '3']
k = 0
while name_first not in good_name_list:
    print("Choose between John and Jack")
    name_first = input()

pencils_number = int(pencils_number_string)
print("|" * pencils_number)

if name_first == "John":
    name_second = "Jack"
    while pencils_number > 0:
        print(name_first + "'s turn:")
        first_pencils_number_string = input()
        good_number_list = ['1', '2', '3']
        y = 1

        while y == 1:
            if first_pencils_number_string.isdigit() == False:
                print("Possible values: '1', '2', '3'")
                y = 1
                first_pencils_number_string = input()
            else:
                if first_pencils_number_string == '0':
                    print("Possible values: '1', '2', '3'")
                    y = 1
                    first_pencils_number_string = input()
                elif int(first_pencils_number_string) < 0:
                    print("Possible values: '1', '2', '3'")
                    y = 1
                    first_pencils_number_string = input()
                elif (first_pencils_number_string in good_number_list and int(first_pencils_number_string) > pencils_number):
                    print("Too many pencils were taken")
                    y = 1
                    first_pencils_number_string = input()
                elif first_pencils_number_string not in good_number_list:
                    print("Possible values: '1', '2', '3'")
                    y = 1
                    first_pencils_number_string = input()
                elif pencils_number - int(first_pencils_number_string) == 0:
                    name_first = name_second
                    y = 0
                    pencils_number = pencils_number - int(first_pencils_number_string)
                else:
                    first_pencils_number = int(first_pencils_number_string)
                    print("|" * (pencils_number - first_pencils_number))
                    print(name_second + "'s turn:")

                    if (pencils_number - first_pencils_number) % 4 == 0:
                        second_pencils_number = 3
                        print(second_pencils_number)
                        print("|" * (pencils_number - first_pencils_number - second_pencils_number))
                        pencils_number = pencils_number - first_pencils_number - second_pencils_number
                        y = 0
                    elif (pencils_number - first_pencils_number) % 4 == 2:
                        second_pencils_number = 1
                        print(second_pencils_number)
                        print("|" * (pencils_number - first_pencils_number - second_pencils_number))
                        pencils_number = pencils_number - first_pencils_number - second_pencils_number
                        y = 0
                    elif (pencils_number - first_pencils_number) % 4 == 3:
                        second_pencils_number = 2
                        print(second_pencils_number)
                        print("|" * (pencils_number - first_pencils_number - second_pencils_number))
                        pencils_number = pencils_number - first_pencils_number - second_pencils_number
                        y = 0

                    elif pencils_number - first_pencils_number == 2:
                        second_pencils_number = 1
                        print(second_pencils_number)
                        print("|" * (pencils_number - first_pencils_number - second_pencils_number))
                        pencils_number = pencils_number - first_pencils_number - second_pencils_number
                        y = 0
                    elif pencils_number - first_pencils_number == 1:
                        second_pencils_number = 1
                        print(second_pencils_number)
                        print("|" * (pencils_number - first_pencils_number - second_pencils_number))
                        pencils_number = pencils_number - first_pencils_number - second_pencils_number
                        y = 0
    print(name_first + " won!")


else:
    name_first = "Jack"
    name_second = "John"
    while pencils_number > 0:
        print(name_first + "'s turn:")

        if pencils_number % 4 == 0:
            first_pencils_number = 3
            print(first_pencils_number)
            print("|" * (pencils_number - first_pencils_number))
            pencils_number = pencils_number - first_pencils_number
            if pencils_number == 0:
                name_first = "John"
        elif pencils_number % 4 == 3:
            first_pencils_number = 2
            print(first_pencils_number)
            print("|" * (pencils_number - first_pencils_number))
            pencils_number = pencils_number - first_pencils_number
            if pencils_number == 0:
                name_first = "John"
        elif pencils_number % 4 == 2 and pencils_number != 2:
            first_pencils_number = 1
            print(first_pencils_number)
            print("|" * (pencils_number - first_pencils_number))
            pencils_number = pencils_number - first_pencils_number
            if pencils_number == 0:
                name_first = "John"
        elif pencils_number % 4 == 1 and pencils_number != 1:
            first_pencils_number = 3
            print(first_pencils_number)
            print("|" * (pencils_number - first_pencils_number))
            pencils_number = pencils_number - first_pencils_number
            if pencils_number == 0:
                name_first = "John"
        elif pencils_number == 2:
            first_pencils_number = 1
            print(first_pencils_number)
            print("|" * (pencils_number - first_pencils_number))
            pencils_number = pencils_number - first_pencils_number
            if pencils_number == 0:
                name_first = "John"
        elif pencils_number == 1:
            first_pencils_number = 1
            print(first_pencils_number)
            print("|" * (pencils_number - first_pencils_number))
            pencils_number = pencils_number - first_pencils_number
            if pencils_number == 0:
                name_first = "John"


        w = 1
        if pencils_number == 0:
            w = 0
        else:
            print(name_second + "'s turn:")
            second_pencils_number_string = input()
            good_number_list = ['1', '2', '3']
            while w == 1:
                if second_pencils_number_string.isdigit() == False:
                    print("Possible values: '1', '2', '3'")
                    w = 1
                    second_pencils_number_string = input()
                else:
                    second_pencils_number = int(second_pencils_number_string)
                    if second_pencils_number_string == '0':
                        #print("The number of pencils should be positive")
                        print("Possible values: '1', '2', '3'")
                        w = 1
                        second_pencils_number_string = input()
                    elif second_pencils_number < 0:
                        #print("The number of pencils should be numeric")
                        print("Possible values: '1', '2', '3'")
                        w = 1
                        second_pencils_number_string = input()
                    elif second_pencils_number_string not in good_number_list:
                        print("Possible values: '1', '2', '3'")
                        w = 1
                        second_pencils_number_string = input()
                    elif (second_pencils_number_string in good_number_list and int(second_pencils_number_string) > pencils_number):
                        print("Too many pencils were taken")
                        w = 1
                        second_pencils_number_string = input()
                    else:
                        print("|" * (pencils_number - second_pencils_number))
                        pencils_number = pencils_number - int(second_pencils_number_string)
                        w = 0
                #pencils_number = pencils_number - first_pencils_number - int(second_pencils_number_string)

    print(name_first + " won!")

'''if pencils_number - int(first_pencils_number_string) == 0:
            print(name_second + " won!")
        elif (pencils_number - first_pencils_number >= 3):
            print("|" * (pencils_number - first_pencils_number))
            print(name_second + "'s turn:")
            second_pencils_number = random.randint(1,3)
        elif (pencils_number - first_pencils_number == 2):
            print("|" * (pencils_number - first_pencils_number))
            print(name_second + "'s turn:")
            second_pencils_number = random.randint(1,2)
        elif (pencils_number - first_pencils_number == 1):
            print("|" * (pencils_number - first_pencils_number))
            print(name_second + "'s turn:")
            second_pencils_number = random.randint(1,1)
            print("|" * (pencils_number - first_pencils_number - second_pencils_number))
            pencil_number = pencils_number - first_pencils_number - second_pencils_number
    print(name_first + " won!")

good_number_list = ['1', '2', '3']
p = 0

while pencils_number > 0:
    print(name_first + "'s turn:")
    first_pencils_number_string = input()

    j = 1
    while j == 1:
        if first_pencils_number_string.isdigit() == False:
            print("Possible values: '1', '2', '3'")
            j = 1
            first_pencils_number_string = input()

        elif (first_pencils_number_string not in good_number_list and int(first_pencils_number_string) < pencils_number):
            print("Possible values: '1', '2', '3'")
            j = 1
            first_pencils_number_string = input()
        elif int(first_pencils_number_string) > pencils_number:
            print("Too many pencils were taken")
            j = 1
            first_pencils_number_string = input()
        else:
            j = 0
        if first_pencils_number_string.isdigit() == False:
            print("Possible values: '1', '2', '3'")
            j = 1
            first_pencils_number_string = input()
        elif first_pencils_number_string.isdigit() == True:
            if first_pencils_number_string == '0':
                print("Possible values: '1', '2', '3'")
                j = 1
                first_pencils_number_string = input()
            if int(first_pencils_number_string) > pencils_number:
                print("Too many pencils were taken")
                j = 1
                first_pencils_number_string = input()
            elif int(first_pencils_number_string) < 0:
                print("Possible values: '1', '2', '3'")
                j = 1
                first_pencils_number_string = input()
            elif (int(first_pencils_number_string) > 3 and int(first_pencils_number_string) < pencils_number):
                print("Possible values: '1', '2', '3'")
                first_pencils_number_string = input()
                j = 1
            else:
                j = 0
        #first_pencils_number = int(first_pencils_number_string)

    if pencils_number - int(first_pencils_number_string) == 0:
        print(name_second + " won!")
    elif (pencils_number - int(first_pencils_number_string) > 0):
        print("|" * (pencils_number - int(first_pencils_number_string)))
        print(name_second + "'s turn:")
        second_pencils_number_string = input()

        l = 1
        while l == 1:
            if second_pencils_number_string.isdigit() == False:
                print("Possible values: '1', '2', '3'")
                l = 1
                second_pencils_number_string = input()

            elif (second_pencils_number_string not in good_number_list and int(second_pencils_number_string) < pencils_number):
                print("Possible values: '1', '2', '3'")
                l = 1
                second_pencils_number_string = input()

            elif int(second_pencils_number_string) > pencils_number - int(first_pencils_number_string):
                print("Too many pencils were taken")
                l = 1
                second_pencils_number_string = input()
            elif pencils_number - int(first_pencils_number_string) - int(second_pencils_number_string) == 0:
                print(name_first + " won!")
                l = 0
            else:
                print("|" * (pencils_number - int(first_pencils_number_string) - int(second_pencils_number_string)))
                l = 0
            if second_pencils_number_string.isdigit() == False:
                print("Possible values: '1', '2', '3'")
                l = 1
                second_pencils_number_string = input()
            else:
                if second_pencils_number_string == '0':
                    print("Possible values: '1', '2', '3'")
                    l = 1
                    second_pencils_number_string = input()
                elif int(second_pencils_number_string) < 0:
                    print("Possible values: '1', '2', '3'")
                    l = 1
                    second_pencils_number_string = input()
                elif int(second_pencils_number_string) > pencils_number - int(first_pencils_number_string):
                    print("Too many pencils were taken")
                    l = 1
                    second_pencils_number_string = input()
                elif (int(second_pencils_number_string) > 3 and int(second_pencils_number_string) < pencils_number - int(first_pencils_number_string)):
                    print("Possible values: '1', '2', '3'")
                    second_pencils_number_string = input()
                    l = 1
                else:
                    l = 0


    pencils_number -= (int(first_pencils_number_string) + int(second_pencils_number_string))




#if (name_first == "John" and p % 2 == 1):
    #print("Jack won!")
#elif (name_first == "John" and p % 2 == 0):
    #print("John won!")
#else:
    #print("John won!")'''

'''while y == 1:
            if first_pencils_number_string.isdigit() == False:
                #print("The number of pencils should be numeric")
                print("Possible values: '1', '2', '3'")
                y = 1
                first_pencils_number_string = input()
            elif int(first_pencils_number_string) == 0:
                #print("The number of pencils should be positive")
                print("Possible values: '1', '2', '3'")
                y = 1
            else:
                first_pencils_number = int(first_pencils_number_string)
                if first_pencils_number = 0:
                    #print("The number of pencils should be positive")
                    print("Possible values: '1', '2', '3'")
                    y = 1
                    first_pencils_number_string = input()
                elif first_pencils_number < 0:
                    #print("The number of pencils should be numeric")
                    print("Possible values: '1', '2', '3'")
                    y = 1
                    first_pencils_number_string = input()
                elif (first_pencils_number not in good_number_list and first_pencils_number < pencils_number):
                    print("Possible values: '1', '2', '3'")
                    y = 1
                    first_pencils_number_string = input()
                elif first_pencils_number > pencils_number:
                    print("Too many pencils were taken")
                    y = 1
                    first_pencils_number_string = input()
                else:
                    y = 0
                    if pencils_number - first_pencils_number == 0:
                        print(name_second + " won!")
                    elif pencils_number - first_pencils_number >= 3:
                        print("|" * (pencils_number - first_pencils_number))
                        print(name_second + "'s turn:")
                        second_pencils_number = random.randint(1,3)

                    elif (pencils_number - first_pencils_number == 2):
                        print("|" * (pencils_number - first_pencils_number))
                        print(name_second + "'s turn:")
                        second_pencils_number = random.randint(1,2)

                    elif (pencils_number - first_pencils_number == 1):
                        print("|" * (pencils_number - first_pencils_number))
                        print(name_second + "'s turn:")
                        second_pencils_number = random.randint(1,1)
                    print(second_pencils_number)
                    print("|" * (pencils_number - first_pencils_number - second_pencils_number))
        #print("|" * (pencils_number - first_pencils_number - second_pencils_number))
            pencils_number = pencils_number - first_pencils_number - second_pencils_number
    print(name_first + " won!")'''



'''if (pencils_number - first_pencils_number >= 5 and (pencils_number - first_pencils_number) % 5 == 0 and (pencils_number - first_pencils_number) % 4 != 0 and (pencils_number - first_pencils_number) % 3 != 0 and (pencils_number - first_pencils_number) % 2 != 0):
                        second_pencils_number = 2
                        print(second_pencils_number)
                        print("|" * (pencils_number - first_pencils_number - second_pencils_number))
                        pencils_number = pencils_number - first_pencils_number - second_pencils_number
                        y = 0
                    elif (pencils_number - first_pencils_number >= 5 and (pencils_number - first_pencils_number) % 4 == 0):
                        second_pencils_number = 3
                        print(second_pencils_number)
                        print("|" * (pencils_number - first_pencils_number - second_pencils_number))
                        pencils_number = pencils_number - first_pencils_number - second_pencils_number
                        y = 0
                    elif (pencils_number - first_pencils_number >= 5 and (pencils_number - first_pencils_number) % 4 != 0 and (pencils_number - first_pencils_number) % 3 == 0 and (pencils_number - first_pencils_number) % 2 != 0):
                        second_pencils_number = 2
                        print(second_pencils_number)
                        print("|" * (pencils_number - first_pencils_number - second_pencils_number))
                        pencils_number = pencils_number - first_pencils_number - second_pencils_number
                        y = 0
                    elif (pencils_number - first_pencils_number >= 5 and (pencils_number - first_pencils_number) % 4 != 0 and (pencils_number - first_pencils_number) % 3 != 0 and (pencils_number - first_pencils_number) % 2 == 0):
                        second_pencils_number = 1
                        print(second_pencils_number)
                        print("|" * (pencils_number - first_pencils_number - second_pencils_number))
                        pencils_number = pencils_number - first_pencils_number - second_pencils_number
                        y = 0
                    elif (pencils_number - first_pencils_number >= 5 and (pencils_number - first_pencils_number) % 4 != 0 and (pencils_number - first_pencils_number) % 3 == 0 and (pencils_number - first_pencils_number) % 2 == 0):
                        second_pencils_number = 1
                        print(second_pencils_number)
                        print("|" * (pencils_number - first_pencils_number - second_pencils_number))
                        pencils_number = pencils_number - first_pencils_number - second_pencils_number
                        y = 0
                    elif (pencils_number - first_pencils_number >= 5 and (pencils_number - first_pencils_number) % 5 != 0 and (pencils_number - first_pencils_number) % 4 != 0 and (pencils_number - first_pencils_number) % 3 != 0 and (pencils_number - first_pencils_number) % 2 != 0):
                        second_pencils_number = 2
                        print(second_pencils_number)
                        print("|" * (pencils_number - first_pencils_number - second_pencils_number))
                        pencils_number = pencils_number - first_pencils_number - second_pencils_number
                        y = 0
                    elif pencils_number - first_pencils_number == 4:
                        second_pencils_number = 3
                        print(second_pencils_number)
                        print("|" * (pencils_number - first_pencils_number - second_pencils_number))
                        pencils_number = pencils_number - first_pencils_number - second_pencils_number
                        y = 0'''


'''elif pencils_number - first_pencils_number == 3:
                        second_pencils_number = 2
                        print(second_pencils_number)
                        print("|" * (pencils_number - first_pencils_number - second_pencils_number))
                        pencils_number = pencils_number - first_pencils_number - second_pencils_number
                        y = 0'''


'''if pencils_number >= 5:
            first_pencils_number = 1
            print(first_pencils_number)

        elif pencils_number == 4:
            first_pencils_number = 3
            print(first_pencils_number)

        elif pencils_number == 3:
            first_pencils_number = 2
            print(first_pencils_number)

        elif pencils_number == 2:
            first_pencils_number = 1
            print(first_pencils_number)'''
