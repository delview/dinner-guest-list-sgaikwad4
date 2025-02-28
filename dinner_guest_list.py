# Create lists
guests = []

# function to print sorted list
def print_sorted_list():
    guests.sort()
    for guest in guests:
        print(f"Here are the guests: {guest}")
    
    while True:
        choice = input("\nDo you want to [R]emove or [A]dd a person or send [I]]nvitations?").strip().title()
        if choice == "R":
            remove()
            break
        elif choice == "A":
            pass
        elif choice == "I":
            send_invitations()
            break
        else:
            print("Please enter a valid answer")

# function to replace someone
def remove():
    while True:
        try:
            guests.remove(input("Who do you want to remove? ").strip().title())

            print_sorted_list()
            break
        except:
            print("The name you entered was not found in the list")

def send_invitations():
    for guest in guests:
        print(f"Hello {guest}. You have been invitated for dinner")
    
    

# Ask user for amount of guests they want to invite 
while True:
    try:
        num_of_guests = int(input("How many guests do you want to invite?\n").strip())
        break
    except ValueError:
        print("Please enter a number")
# Create loop that will keep apending names to the list until the limit is met
for guest in range(num_of_guests):
    guest = input(f"Enter the name of guest #{guest+1}: ").strip().title()
    guests.append(guest)
print_sorted_list()