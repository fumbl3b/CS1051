prompt = '''
Please give me an integer amount of seconds and I will convert it to it\'s 
equivalent hours, minutes, and seconds'''
print(prompt)
seconds = int(input())

# 1 hour = 3600 seconds
hours = seconds // 3600
# 1 minute = 60 seconds
# take remainder of after hours
minutes = (seconds % 3600) // 60
# take the remainder of minutes (since this will also account for hours)
result_seconds = seconds % 60
print(f'{seconds} seconds = {hours} hours, {minutes} minutes, and {result_seconds} seconds')