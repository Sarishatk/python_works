"""
*args recieve parameter as a tuple
**kwargs recieve parameter as a dictionary
 
"""

def add_numbers(*args):

    return sum(args)

print(add_numbers(23,40))
print(add_numbers(10,20,-45))



def display_person_details(*args):
    print(args)
    name = args[0]
    address = args[1]

    print(name)
    print(address)


display_person_details("james","street1","uk","landon",3532456)


def display_person_details(**args):

    print(args)

display_person_details(name = "james",rollno = 3532456, place = "london")