'''
    In this scenario, we have a directory with 5 files in it.
    Each file has a different size: 2048, 4357, 97658, 125, and 8. 
    Fill in the blanks to calculate the average file size by having Python add all the values for you, 
    and then set the files variable to the number of files. Finally, output a message saying "The average size is: " followed by the resulting number. 
    Remember to use the str() function to convert the number into a string. 
'''

total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is:" + str(average))

# why variabel average converg to str ?
# because impossible when add the text
# the text is "The average size is:"
# this is explicit conversion


print("\n another case")
# The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests 
 
# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) # change a data type


print('\nwhen use connector alternative in expression')
# The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
 
print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.
 
# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string.

print('\nresolve zero division error')
numerator = 7
denominator = 0  # Possible resolution: Change the denominator value --> 1
result = numerator / denominator
print(result)
 
# One possible assumption for a number divided by zero error might
# include the issue of a null value as a denominator (could happen when
# using a loop to iterate over values in a database). In such cases, the
# desired outcome may be to leave the numerator value intact. The
# numerator value can be preserved by reassigning the denominator with 
# the integer value of 1. The result would then equal the numerator.