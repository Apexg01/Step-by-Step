name = input("What's your good name? ")
print("Hello, "+name+"! Please enter the date, month & year in dd mm yyyy format as per the requirement.")

date = int(input("What's today's date? "))
mo = input("Whats's the month going on? ")
ye = input("What's the year going on? ")

if mo == "1" or mo == "01":
    month = int(31)
if mo == "2" or mo == "02":
    month = int(59)  
if mo == "3" or mo == "03":
    month = int(90) 
if mo == "4" or mo == "04":
    month = int(120)     
if mo == "5" or mo == "05":
    month = int(151)
if mo == "6" or mo == "06":
    month = int(181)
if mo == "7" or mo == "07":
    month = int(212)
if mo == "8" or mo == "08":
    month = int(243)
if mo == "9" or mo == "09":
    month = int(273)
if mo == "10":
    month = int(304)
if mo == "11":
    month = int(334)
if mo == "12":
    month = int(365)

days_completed = date + month 


#close thr "" and use variable with + on both sides to use it in constant sentence perfectly
print("Please enter your Date of birth as per the column")

dd = int(input("Enter your *DATE* of birth:- "))
mm = input("Enter your *MONTH* of birth:- ")
yyyy = input("Enter your *YEAR* of birth:- ")

if mm == "1" or mm == "01":
    month = int(31)
if mm == "2" or mm == "02":
    month = int(59)  
if mm == "3" or mm == "03":
    month = int(90) 
if mm == "4" or mm == "04":
    month = int(120)     
if mm == "5" or mm == "05":
    month = int(151)
if mm == "6" or mm == "06":
    month = int(181)
if mm == "7" or mm == "07":
    month = int(212)
if mm == "8" or mm == "08":
    month = int(243)
if mm == "9" or mm == "09":
    month = int(273)
if mm == "10":
    month = int(304)
if mm == "11":
    month = int(334)
if mm == "12":
    month = int(365)

day_trageted = dd + month

days_left = day_trageted - days_completed - 1

if days_left < 0:
    corr= int(365) + days_left + 1
    print("Your birthday has already passed this year, but don't worry! Your next birthday is in "+str(corr)+" days.")
else:
    print("Your birthday is in "+str(days_left)+" days. Get ready to celebrate!")


if days_left < 0:
     years= int(ye) - int(yyyy) 
else:     
     years= int(ye) - int(yyyy) -1 

nx_yr= int(years) + 1 
print("You are currently "+str(years)+" years old. Happy "+str(nx_yr)+"th Birthday in advance " +name+"! :)")