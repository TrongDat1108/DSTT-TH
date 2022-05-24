#cau A
def masterNumber(birthday: str):
    master = 0
    date = birthday.split('/')
    for index in date:
        temp = int(index)
        while temp != 0:
            master += temp % 10
            temp = int(temp / 10)
    if master > 10:
        master = (master % 10) + (int(master / 10))
    return master
#cau B
def yourPersonalYearNumber(birthday: str, year: int):
    result = 0
    temp = 0
    date = birthday.split('/')
    for i in range(2):
        element = int(date[i])
        while element != 0:
            temp += element % 10
            element = int(element / 10)
    while year != 0:
        temp += year % 10
        year = int(year / 10)
    while temp != 0:
        result += temp % 10
        temp = int(temp / 10)
    return result

#cau C
def destinyNumber(name: str):
    temp = 0
    name = name.upper()
    for char in name:
        if ord(char) != 32:
            temp += (ord(char) - 65 + 1) % 9

    result = temp
    
    while result >= 10 and result != 11 and result != 22:
        temp = result
        result = 0
        while temp != 0:
            result += temp % 10
            temp = int(temp / 10)
    return result

#cau D
def soulNumber(name: str):
    temp = 0
    name = name.upper()
    for i in range(len(name)):
        char = name[i]
        if char == 'Y' and name[i-1] == 'U' and i > 1:
            pass
        elif ord(char) != 32 and "UEOAIY".find(char) != -1:
            temp += (ord(char) - 65 + 1) % 9

    result = temp
    while result > 11:
        temp = result
        result = 0
        while temp != 0:
            result += temp % 10
            temp = int(temp / 10)
    return result

#cau E
def impressionNumber(name: str):
    temp = 0
    name = name.upper()
    for i in range(len(name)):
        char = name[i]
        if char == 'Y' and name[i-1] == 'U' and i > 1:
            temp += (ord(char) - 65 + 1) % 9
        elif ord(char) != 32 and "UEOAIY".find(char) == -1:
            temp += (ord(char) - 65 + 1) % 9

    result = temp
    while result > 11:
        temp = result
        result = 0
        while temp != 0:
            result += temp % 10
            temp = int(temp / 10)
    return result
        

date = input("Please enter your birthday (e.g 19/08/1999): ")
name = input("Please enter your full name (e.g Nguyen Trong Dat): ")
print("Cau A Your master number is: ",masterNumber(date))
print("Cau B Your personal year number in 2022 is: ",yourPersonalYearNumber(date, 2022))
print("Cau C Your destiny number is: ",destinyNumber(name))
print("Cau D Your soul number is: ", soulNumber(name))
print("Cau E Your impression number is: ", impressionNumber(name))
