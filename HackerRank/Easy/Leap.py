# any year divisible by 400 and 4 is a leap year

year = int(input())
#return year

# creating a function is_leap to identify leap year from given input

def is_leap() :
    if year/4 == 0 :
        if year/400 == 0 :
            print(f'{year} is a leap year')
    else :
    print(f'{year} is not a leap year')
