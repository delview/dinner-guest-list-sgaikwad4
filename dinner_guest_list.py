# Create lists
guests = []

# function to print sorted list
def print_sorted_list():
    guests.sort()
    for guest in guests:
        print(guest)
    choice = input("Do you want to replace someone? [y]es or [n]o? ")
    if choice == "y":
        replace()
    else:
        print("why not")
# function to replace someone
def replace():
    guests.remove(input("Who do you want to replace? "))
    guests.append(input("Who's the new guest? "))
    print_sorted_list()
# Ask user for amount of guests they want to invite 
num_of_guests = int(input("How many guests do you want to invite?\n"))

# Create loop that will keep apending names to the list until the limit is met
for guest in range(num_of_guests):
    guest = input(f"Enter the name of guest #{guest+1}: ")
    guests.append(guest)
print_sorted_list()


