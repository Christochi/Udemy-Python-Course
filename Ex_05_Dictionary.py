# A Dictionary are like list but they are organised by keys or properties instead of by index

# Each component of a Dictionary is composed by a key value pair

# for example: person = { "first_name":"John", "last_name":"Green", "birth_year":1980, "country_of_birth":"Canada" }

# to get a value: person["last_name"]

# Dictionaries are mutable in python: person["birth_year"] = 1979

# to add new key: person["marital_status"] = "Married"

# values of a dictionary can be of any data type including tuples, dictionary, list

# a list of dictionary: person["children"] = ["Nathalie", "Ethan"]

# add to the list of children: person["children"].append("Jean")

# get function is used to retrieve a property of a dictionary and if it doesn't exit,
# an optional error message can be included. get function is used to avoid runtime error message
# person.get("age", "invalid property")

# another useful example: key = "first_name", person[key]

# to erase information from a dictionary: person.clear()

print( "Program asks the users what information they wants, then print the value"
           + " associated to that key or display a message in case they key is not found" )
print( "\n")

# predefined dictionary
person = { "name":"Toks", "age":29, "address":"ottawa", "phone":"555" }

# lower method will transform user input to lower case
info = input( "What would you like to know: " ).lower()

# takes the key in info to retrieve the value of the key. If wrong key is
# inputted, the get function prints "invalid request"
print( person.get( info, "invalid request" ) )

