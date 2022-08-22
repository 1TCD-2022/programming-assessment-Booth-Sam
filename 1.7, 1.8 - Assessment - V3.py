"""
Filename: Theme Park Program for Staff Use
Author: Sam Booth
Date: 28/06/2022
Description: Program for staff at the theme park to use to find the entrance
             price for visitors and the rides they are allowed to use.
"""
import random

# Functions to validate inputs
def entrance_level_validation(entrance_levels):
    while True:
        group_level = input("Enter group entrance level ")
        if group_level.lower().strip() in entrance_levels:
            return group_level.lower().strip()
        else:
            print("Please enter a valid entrance level ")
def members_validation():
    while True:
        try:
            group_members = int(input("Enter number of members in the group "))
            return group_members
        except ValueError:
            print("Please enter a number of group members")

def height_validation(name):
    while True:
        try:
            person_height = int(input("Enter the height of {} in cm ".format(name)))
            if person_height in range(1,300):
                return person_height
        except ValueError:
            print("Please enter a number of cm")

def name(index):
    while True:
        person_name = input("What is the name of person {} ".format(index+1))
        if len(person_name.strip()) > 0:
            return person_name
        else:
            print("Please enter your name")

#Function to work out which rides are available for an individual
def rides_available(person_height, height_restrictions):
    rides_available = 0

    for index1 in range(len(height_restrictions)):
        if person_height > height_restrictions[index1]:
            rides_available = rides_available+1
    return rides_available
    
#Function to work out if a group is entitled to free ice cream according to their entrance level
def ice_cream(group_level):
    if len(group_level)<5:
        return "0"
    elif len(group_level) == 5:
        return "1"
    elif len(group_level)>5:
        return "unlimited"

#Function to work out price for group
def price(group_level, group_members):
    #Work out price based on $5 for each person times len of the entrance level
    group_price = len(group_level.strip())*5*group_members
    return group_price

#Function giving a group a chance to skip ahead in the queue for a random ride
def queue_skip(group_level):
    #Chance of skipping ahead for each entrance level
    if len(group_level) == 3:
        chance = 0
    elif len(group_level) == 4:
        chance = 40
    elif len(group_level) == 5:
        chance = 60
    elif len(group_level) == 6:
        chance = 100
    #Determine randomly whether a group skips to the front and return a boolean
    output = random.randrange(0,100)
    if output in range(0,chance):
        output = True
    else:
        output = False
    return output
def main():
    #Set lists - entrance levels, rides
    rides = ["Hakuna Matata", "A Walk in the Park",
             "The Bulldog", "Mr Rager", "Hell's Kitchen", "Kilamanjaro",
             "Stampede", "The Drop", "Don't Look Down", "Bronco"]
    height_restrictions = [80, 80, 110, 120, 120, 120, 150, 150, 150, 160]
    entrance_levels = ["red", "pink", "green", "yellow"]
        
    #Print entrance levels
    print(""""The available entrance levels are {}
    The higher entrance levels(more letters) have more perks.
    These include a higher chance to skip to the front of the queue
    and free ice creams!!""".format(entrance_levels))

    #Ask what level of entrance the group is and validate this
    group_level = entrance_level_validation(entrance_levels)

    #Ask how many members there are in the group and validate this

    group_members = members_validation()
    
    #Ask the names and heights(cm) of each member in the group
    #Work out which rides each member is able use by which requirements they meet
    #Requirements - height
    for index in range(group_members):

        person_name = name(index)
            
        person_height = height_validation(person_name)
        
        print("{} can use the rides: {}".format(person_name, rides[0:rides_available(person_height, height_restrictions)]))
        print()

    

    #Print total price of group entrance
    print("The price for your group is ${}".format(price(group_level, group_members)))

    #Print number of free ice creams available for group
    print("Your group is allowed {} free ice cream(s) per person".format(ice_cream(group_level)))

    #Print ride available for group to skip to the front of (if appicable)
    if queue_skip(group_level):
        print("Your group is allowed to skip to the front of {}".format(random.choice(rides)))
main()
