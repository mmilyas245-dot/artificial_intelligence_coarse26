
fullname1=input("enter full name:")
totalname=fullname1.split(" ")
firstname=totalname[0]
dash=fullname1.find(" ")
lastname=fullname1[dash::]
print("first name : ",firstname)
print("last name : ",lastname)
print("full name is : ",fullname1)