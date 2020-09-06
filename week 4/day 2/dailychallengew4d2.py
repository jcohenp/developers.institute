from datetime import datetime
date = datetime.today()
date = datetime.today().strftime('%Y-%m-%d')
current_datelist = date.split('-')

bday = input('your bday please year-month-day\n')
datelist = bday.split('-')

c_year = int(current_datelist[0])
c_month = int(current_datelist[1])
c_day = int(current_datelist[2])
year = int(datelist[0])
month = int(datelist[1])
day = int(datelist[2])

age = c_year - year - ((c_month, c_day) < (month, day))

num_list = list(str(age))

num = int(num_list[-1])
candles = ''
for i in range(num):
    candles += 'i'

print("    __"  + candles + "__")
print("   |:H:a:p:p:y|")
print(" __|__________|__")
print("|^^^^^^^^^^^^^^^^|")
print("|:B:i:r:t:h:d:a:y|")
print("|                |")
print("~~~~~~~~~~~~~~~~~~")


