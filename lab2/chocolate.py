print("Welcome to the Chocolate bar estimator")
weight = float(input("Please enter your weight in lbs: "))
height = float(input("Please enter your height in inches: "))
age = float(input("Please enter your age in years: "))

BMR_FEMALE = 655.1 + (4.35 * weight) + (4.7 * height) - (4.7 * age)
BMR_MALE = 66 + (6.2 * weight) + (12.7 * height) - (6.76 * age)
print("If you are a man, you must eat " + str(round(BMR_MALE/214, 2)) + " candy bars a day to maintain your current weight")
print("If you are a woman, you must eat " + str(round(BMR_FEMALE/214, 2)) + " candy bars a day to maintain your current weight")
