from replit import clear

# logo of gavel just for UI
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

# defining function that adds item to the dictionary
def bid_add(name,bid):
  bids[name] = bid

# welcome line
print("Welcome to the secret auction program")

# setting the program to true to loop
run = True

# creating an empty dict
bids = {}

# clearing console to keep clean terminal
clear()


# looping till all users are added to the dictionary
while run is True:
  print(logo)
  name = input("What's your name?\n")
  bid = float(input("What's your bid? \n$"))
  bid_add(name,bid)
  add_user = input("Are there any other people to bid?\nReply 'Yes' or 'no'\n").lower()

  # checking to see if there are more bidders
  if add_user == "no":
    run = False

  # clearing console if there are more users
  elif add_user == "yes":
    clear()
  

# creating a seperate dictionary for the max value from bids dictionary
winning_bid = max(bids)
bid_price = bids[winning_bid]

print(f"The winner is {winning_bid} with a bid of ${bid_price} ")
