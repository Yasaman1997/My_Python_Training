zoo_animals = ["pangolin", "cassowary", "sloth", "dog"];
# One animal is missing!

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]




animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")  # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra")

print animals  # Observe what prints after the insert operation







start_list = [5, 3, 1, 2, 4]
square_list = []



# Your code here!
for x in start_list:

    square_list.append(x**2)
square_list.sort()
print square_list
my_list = [1, 9, 3, 8, 5, 7]

for number in my_list:
    # Your code here
    for number in my_list:
        print   2 * number




# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number
print residents['Sloth']
print residents['Puffin'] # Prints Puffin's room number
print residents['Burmese Python']









menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['pizza'] = 2.50
menu['soup'] = 1.50
menu['Salad'] = 5.50


print "There are " + str(len(menu)) + " items on the menu."
print menu