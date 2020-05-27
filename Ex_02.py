# x[start:end] items start through end-1, myString[0:2]
# x[start:] items start through the rest of the list, myString[-2:]
# x[:end] items from the beginning through end-1, myString[:3]
# x[:] a copy of the whole list

print( "Exercise 1: Program asks the user for first name, middle name and surname"
       + ", then prints initials" )

fName = input( "Please enter first name: " ) 
mName = input( "Please enter middle name: " ) 
lName = input( "Please enter last name: " ) 

print( "Your initials are", fName[0:1] + mName[0:1] + lName[0:1] )

print( "\n" )
print( "Exercise 2: Program prints country code, product code, batch number of a product" )

lotNumber = "037-00901-00027"

print( "Country code:", lotNumber[:3] )
print( "Product code:", lotNumber[4:9] )
print( "Batch number:", lotNumber[10:] )
