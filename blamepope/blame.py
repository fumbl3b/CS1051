user_input = input("Please enter a date in MM/DD/YYYY format: ")


#            0123456789
# ex_date = "10/01/1990"

date = user_input.split('/')
month = date[0]
day = date[1]
year = date[2]

def validate_date(m, d, y):
    if int(m) not in range(12): return False
    if int(d) not in range(31): return False
    if int(y) < 0: return False
    return True

print(validate_date(month, day, year))
if not validate_date(month, day, year):
    print("date is invalid")
else: print(month, day, year)
