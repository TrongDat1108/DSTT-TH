x = input('Enter your birthday: ')
birthday = x.split('/')

def ex7(day, month):
    if (day >= 1 and day <= 31 and month >= 1 and month <= 12):
        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return 'Aries (Ram)'
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return 'Taurus (Bull)'
        elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
            return 'Gemni (Twins)'
        elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
            return 'Cancer (Crab)'
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return 'Leo (Lion)'
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return 'Virgo (Virgin)'
        elif (month == 9 and day >= 22) or (month == 10 and day <= 23):
            return 'Libra (Balance)'
        elif (month == 10 and day >= 24) or (month == 11 and day <= 21):
            return 'Scorpius (Scorpion)'
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return 'Sagittarius (Archer)'
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            return 'Capricornus (Goat)'
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return 'Aquarius (Water Bearer)'
        elif (month == 2 and day >=19) or (month == 3 and day <= 20):
            return 'Piscres (Fish)'

print(ex7(int(birthday[0]), int(birthday[1])))
