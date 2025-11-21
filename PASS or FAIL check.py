print("Hello Student!, Enter your marks to check if you are PASS or FAIL")
phy = int(input("Enter marks of Physics: "))
chem = int(input("Enter marks of Chemistry: ")) 
math = int(input("Enter marks of Mathematics: "))
opt = int(input("Enter marks of Optional Subject: "))

x = (phy+chem+math+opt) /2 
y = x - 33

if x >= 33:
    print("PASS")
    print("Congratulations!,You have passed by", y ,"marks")

else:
    print("FAIL")   
    print("You have failed by", y, "marks")

print("Your total marks are", x)

# , seperates      