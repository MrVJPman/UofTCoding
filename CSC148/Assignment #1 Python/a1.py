import sys
import os
import random

# Seed random number generator so output is deterministic
random.seed(0)

from convenience import Refrigerator, Drink, AmbivalentCustomer, \
    SimpleCustomer, DeterminedCustomer

# useful dictionary for converting between customer types and customer classes
CUSTOMER_TYPES = {'ambivalent': AmbivalentCustomer,
                  'simple': SimpleCustomer,
                  'determined': DeterminedCustomer}


def prompt_filename():
    """Prompt user for filename until name of existing file is provided"""
    while True:
        print >>sys.stderr, "Enter the input file name: ",
        filename = 'sample_input3.txt'
        if os.path.isfile(filename):
            return filename
        else:
            print >>sys.stderr, "Cannot find file: %r" % filename

if __name__ == '__main__':
    refrigerator = None
    unstocked_drinks = []
    day = 1
    filename = prompt_filename()
    for line in open(filename):
        line = line.strip()
        if not line:
            continue

        print "Processing command: %r" % line
        if line.startswith('shelves'):
            # Create shelves of appropriate sizes
            shelf_sizes = [int(size) for size in line.split()[1:]]
            refrigerator = Refrigerator(shelf_sizes)
        elif line.startswith('drink'):
            # Add a new drink to the list waiting to be stocked
            name, expiration = line.split()[1:]
            unstocked_drinks.append(Drink(name, int(expiration)))
        elif line.startswith('load'):
            # Stock any unstocked drinks
            refrigerator.stock_drinks(unstocked_drinks)
            print ("Stocked refrigerator with %d drinks."
                   % len(unstocked_drinks))
        elif line.startswith('customer'):
            # Have the customer try to get a drink
            kind = line.split()[1]
            customer = CUSTOMER_TYPES[kind.lower()]()
            drink = customer.get_drink(refrigerator)
            if drink is None:
                print "%s customer left with nothing." % kind
            else:
                print "%s customer bought %s." % (kind, drink)
        elif line.startswith('new_day'):
            # It's a new day! Age all the drinks and remove any that expired.
            day += 1
            refrigerator.age_drinks()
            n_culled = refrigerator.cull_drinks()
            if n_culled:
                print "Day %d: Found %d expired drinks." % (day, n_culled)
            else:
                print "Day %d: All drinks are still good." % day
        else:
            print >>sys.stderr, "Error: unknown command %r" % line
            sys.exit(1)

        # Uncomment the line below to print the state of the refrigerator
        # after every command. This could be extremely useful for debugging.
        # print refrigerator
