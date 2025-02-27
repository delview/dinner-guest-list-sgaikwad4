# Create lists
num_of_guests = []
guests = []

# function to print sorted list
def print_sorted_list():
    guests.sort()
    print(guests)

# function to replace someone

# Ask user for amount of guests they want to invite 
num_of_guests = int(input("How many guests do you want to invite?\n"))

# Create loop that will keep apending names to the list until the limit is met
for guest in range(num_of_guests):
    guest = input(f"Enter the name of guest #{guest+1}")
    guests.append(guest)
print_sorted_list()


