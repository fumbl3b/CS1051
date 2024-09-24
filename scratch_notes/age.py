my_thirties = range(30, 40)
time_left_in_thirties = 10.0

for year in my_thirties:
    print(f"i am {year} years old")
    for month in range(1,13):
        # print(f"I am {year} and {month} month(s) old")
        time_left_in_thirties = 40 - (year + (month/12))
        print(f"I have {time_left_in_thirties} years left in my 30s")
        if(time_left_in_thirties <= 10*(2/3)):
            print(f"Its my {month} month in my {year} year, and I am no longer in my early thirties")
            break
        # if (time_left_in_thirties <=(10*(2/3))):
            # print(f"I am {year} years and {month} months old, but I'm still in my early thirties")
