import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
def name_to_number(name):
    if name == "rock":
        name = 0
        return name
    elif name == "Spock":
        name = 1
        return name
    elif name == "paper":
        name = 2
        return name
    elif name == "lizard":
        name = 3
        return name
    elif name == "scissors":
        name = 4
        return name
    else:
        print("Incorrect gesture")

def number_to_name(number):
    if number == 0:
        number = "rock"
        return number
    elif number == 1:
        number = "Spock"
        return number
    elif number == 2:
        number = "paper"
        return number
    elif number == 3:
        number = "lizard"
        return number
    elif number == 4:
        number = "scissors"
        return number
    else:
        print("The number is out of range.")
    
def rpsls(player_choice): 
    print("")
    print ("You've chosen " + str(player_choice))
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print("Computer has chosen " + str(comp_choice))
    
    winner = (comp_number - player_number) % 5
    if (winner == 1) or (winner == 2):
        print("Computer wins!")
    elif (winner == 3) or (winner == 4):
        print("You win!")
    else:
        print("Tie!")
    
# test
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
