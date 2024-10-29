user_input = input("Please enter a date in MM/DD/YYYY format: ")


#            0123456789
# ex_date = "10/01/1990"
#
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def validate_date(date_str):
    if len(date_str) != 10 or date_str[2] != '/' or date_str[5] != '/':
        return "Invalid date format"

    try:
        month = int(date_str[0:2])
        day = int(date_str[3:5])
        year = int(date_str[6:])
    except ValueError:
        return "Invalid date components"

    if not (1 <= month <= 12):
        return "Invalid month"

    if month in [4, 6, 9, 11]:
        if not (1 <= day <= 30):
            return "Invalid day for the given month"
    elif month == 2:
        if is_leap_year(year):
            if not (1 <= day <= 29):
                return "Invalid day for February in a leap year"
        else:
            if not (1 <= day <= 28):
                return "Invalid day for February in a non-leap year"
    else:
        if not (1 <= day <= 31):
            return "Invalid day for the given month"

    return "Valid date"

date_str = input("Enter a date (MM/DD/YYYY): ")
result = validate_date(date_str)
print(result)
