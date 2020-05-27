# tuples and strings are immutable i.e. can't add, remove or change any value
# but list are not

# list uses square brackets while tuples uses normal brackets

# to get number of elements in a list: len(students)

# to retrieve a value in a list or tuple: students[index_num]

# to change an element in a list: students[index_num] = value

# to add element to the list: students.append( "value" )

# elements can be added anywhwere in the list: students.insert( index, "value" )

# remove elements from a list using pop method/function: students.pop()
# just like stack and queue data structure.
# index can be passed: students.pop(0)

# to remove specific element using the remove method: students.remove("Mary")

# to merge 2 lists, use the concat sign (+), e.g., students + students2

# can't merge a list with a tuple

# list and tuples are sequences and they can be of any data type

# functions:
# len, append, insert, pop, remove


print ( "Program asks user for name and then adds it to the end of the list, "
            + "and prints the updated list" )

# predefined list of people
people = [ "Dad", "Mom", "Oby", "Oge", "Oboy", "Chika" ]

# prompt
user = input( "Please enter preferred name: " )

people.append( user )

#print result
print( people )

######################################################################
######################################################################
######################################################################

print( "\n" )

print ( "Program asks user birthday in the format 'DD-MM-YYYY', and then prints "
            + "month of birth" )

months = ( "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" )

# prompt
birthday = input( "Please enter birthday in the format 'DD-MM-YYYY': " )

#get month
month_num = int( birthday[3:5] ) - 1
print(month_num)

print( "You were born in", months[month_num] ) 

