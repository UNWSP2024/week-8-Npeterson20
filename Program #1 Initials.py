# Program #1: Initials
# Write a program that gets a string containing a person's first, middle, and last names, 
# and displays their first, middle, and last initials.  
# For example, if the user enters John William Smith, the program should display J. W. S.



def get_initials(name):
    # Split the name by spaces
    name_parts = name.split()
    # Get the first letter of each part and add a period after it
    initials = '. '.join([part[0].upper() for part in name_parts]) + '.'
    return initials

# Input from user
full_name = input("Enter your full name (first, middle, last): ")
# Display initials
print("Initials:", get_initials(full_name))
