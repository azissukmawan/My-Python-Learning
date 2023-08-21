def mirrored_string(my_string):
    forwards = ""
    backwards = ""

    for character in my_string:

        if character.isalpha():
            forwards += character
            backwards = character + backwards

    if forwards.lower() == backwards.lower():
        return True
    return False


print(mirrored_string("12 Noon"))  # Should be True
print(mirrored_string("Was it a car or cat I saw"))  # Should be False
print(mirrored_string("'eve, Madam Eve"))  # Should be True


print('\n=== example 2 ===')


# This function checks a given schedule entry for an old date and, if
# found, the function replaces it with a new date.
def replace_date(schedule, old_date, new_date):
    # Check if the given "old_date" appears at the end of the given
    # string variable "schedule".
    if schedule.endswith(old_date):
        # If True, the body of the if-block will run. The variable "n" is
        # used to hold the slicing index position. The len() function
        # is used to measure the length of the string "new_date".
        p = len(old_date)

        # The "new_schedule" string holds the updated string with the
        # old date replaced by the new date. The schedule[:-p] part of
        # the code trims the "old_date" substring from "schedule"
        # starting at the final index position (or right-side) counting
        # towards the left the same number of index positions as
        # calculated from len(old_date). Then, the code schedule[-p:]
        # starts the indexing position at the slot where the first
        # character of the "old_date" used to be positioned. The
        # .replace(old_date, new_date) code inserts the "new_date" into
        # the position where the "old_date" used to exist.
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)

        # Returns the schedule with the new date.
        return new_schedule

    # If the schedule does not end with the old date, then return the
    # original sentence without any modifications.
    return schedule


print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024"))
# Should display "Last year’s annual report will be released in March 2024"
print(replace_date("In April, the CEO will hold a conference", "April", "May"))
# Should display "In April, the CEO will hold a conference"
print(replace_date("The convention is scheduled for October", "October", "June"))
# Should display "The convention is scheduled for June"


print('\n=== example 3 ===')

def sales_prices(item_and_price):
    # Initialize variables "item" and "price" as strings
    item = ""
    price = ""
    # Create a variable "item_or_price" to hold the result of the split.
    item_or_price = item_and_price.split()

    # For each element "x" in the split variable "item_or_price"
    for x in item_or_price:

        # Check if the element is a number
        if x.isalpha():

            # If true, assign the element to the "item" string variable and add a space
            # for any item names containing multiple words, like "Winter fleece jacket".
            item += x + " "

        # Else, if x is a number (if x.isalpha() is false):
        else:
            # Assign the element to the "price" string variable.
            price = x

    # Strip the extra space to the right of the last "item" word
    item = item.strip()

    # Return the item name and price formatted in a sentence
    return "{} are on sale for ${}".format(item,price)


# Call to the function
print(sales_prices("Winter fleece jackets 49.99"))
# Should print "Winter fleece jackets are on sale for $49.99"