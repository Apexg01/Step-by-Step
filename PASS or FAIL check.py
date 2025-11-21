print("Supposing, there are only 2 subjects")
phy = int(input("Enter marks of Physics: "))
chem = int(input("Enter marks of Chemistry: ")) 

x = (phy + chem) /2 
y = x - 33

if x >= 33:
    print("PASS")
    print("You have passed by", y ,"marks")

else:
    print("FAIL")   
    print("You have failed by", y, "marks")

print("Your total marks are", x)

# , seperates   