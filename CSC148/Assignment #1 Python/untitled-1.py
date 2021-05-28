from convenience import Refrigerator, Drink, DeterminedCustomer

fridge = Refrigerator([1, 2, 1])
drinks = [Drink('pepsi', 1), Drink('coke', 2), Drink('7-up', 7), Drink('dr pepper', 42)]
customer = DeterminedCustomer()

fridge.stock_drinks(drinks)

print "Refrigerator:\n%s\n" % fridge
print "Determined customer bought: %s\n" % customer.get_drink(fridge)
print "Refrigerator:\n%s" % fridge