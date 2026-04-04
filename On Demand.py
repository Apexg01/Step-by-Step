name = input("Whast's your good name? ")
print("Hello,"+name+"!")
date = input("What's today's date? ")


#close thr "" and use variable with + on both sides to use it in constant sentence perfectly
print("Please enter your Date of birth as per the column")

dd = input("Enter your *DATE* of birth:- ")
mm = input("Enter your *MONTH* of birth:- ")
yyyy = input("Enter your *YEAR* of birth:- ")

if mm == "1" or mm == "01":
    month = int(31)
if mm == "2" or mm == "02":
    month = int(28)  
if mm == "3" or mm == "03":
    month = int(31) 
if mm == "4" or mm == "04":
    month = int(30)     
if mm == "5" or mm == "05":
    month = int(31)
if mm == "6" or mm == "06":
    month = int(30)
if mm == "7" or mm == "07":
    month = int(31)
if mm == "8" or mm == "08":
    month = int(31)
if mm == "9" or mm == "09":
    month = int(30)
if mm == "10":
    month = int(31)
if mm == "11":
    month = int(30)
if mm == "12":
    month = int(31)


time_completed = int(dd) + int(mm)
time_left_in_this_year = 365 - time_completed
