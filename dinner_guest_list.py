# Create lists
guests = []

# function to print sorted list
def print_sorted_list():
    guests.sort()
    for guest in guests:
        print(f"Here are the guests: {guest}")
    
    while True:
        choice = input("\nDo you want to [R]eplace someone or send [I]]nvitations?").strip().title()
        if choice == "R":
            replace()
            break
        elif choice == "I":
            print("invitations have been sent")
            break
        else:
            print("Please enter a valid answer")

# function to replace someone
def replace():
    while True:
        try:
            guests.remove(input("Who do you want to replace? "))
            guests.append(input("Who's the new guest? "))
            print_sorted_list()
            break
        except:
            print("The name you entered was not found in the list")

# Ask user for amount of guests they want to invite 
while True:
    try:
        num_of_guests = int(input("How many guests do you want to invite?\n").strip())
        break
    except ValueError:
        print("Please enter a number")
# Create loop that will keep apending names to the list until the limit is met
for guest in range(num_of_guests):
    guest = input(f"Enter the name of guest #{guest+1}: ")
    guests.append(guest)
print_sorted_list()