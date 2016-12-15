# Python 3.5.2
# Ramon Llull's Thinking Machine Test
# Creates a random entity with a random combination of
# attributes from a given set.
#
# One may increase the disk sizes for further combinations.

import random

# Center
entities = ["God", "Tiger"]
# Disk 1
attributes =  ["Good", "Great", "Eternal", "Powerful", "Wise",
        "Free", "Virtuous", "Truthful", "Glorius"]
colors = ["Black", "White", "Red", "Blue", "Green", "Yellow", 
          "Purple", "Velvet", "Crimson"]

# Helper Methods
def valid_argument(n):
    # TODO: Handle other edge cases as well.
    if (n < 0):
        print ("Illegal Argument: n < 0")
        return False
    else: 
        return True
    
def random_item(a_list):
    item = a_list[random.randrange(0, len(a_list))]
    return item

def combine(description, array):
    """Creates a two-word description from the given array."""
    adverb = random_item(array) + "ly"
    adjective = random_item(array)
    description += adverb + " " + adjective
    return description

# Main Method
def describe(n, array):
    """Describes an entity with an adjective 
    modified by n + (n-1) adverbs."""
    
    # Check Illegal Argument.
    if (valid_argument(n) == False):
        return
    
    # Describe.
    description = ""
    if (n == 0):
        description = random_item(array) + "."
    else:
        for i in range (0, n):
            description = combine(description, array)
            if (i == n-1):
                description += "."
            else:
                description += "ly "
    return description
    

# Test Method
# Increase n in describe(n) for longer descriptions.
def test():
    print ("Ramon Llull's Thinking Machine - Quick Prototype\n")
    print ("The disks revolved heavily, and this was their message:\n")
    print ("The " + random_item(entities) + " is", describe(0, attributes))
    print ()
    print ("The " + random_item(entities) + " is", describe(1, attributes)) 
    print ("The " + random_item(entities) + " is", describe(2, attributes))
    print ("The " + random_item(entities) + " is", describe(3, attributes))
    print ()
    print ("The " + random_item(entities) + " is", describe(0, colors))
    print ()
    print ("The " + random_item(entities) + " is", describe(1, colors)) 
    print ("The " + random_item(entities) + " is", describe(2, colors))
    print ("The " + random_item(entities) + " is", describe(3, colors))
        
# Test
test()
