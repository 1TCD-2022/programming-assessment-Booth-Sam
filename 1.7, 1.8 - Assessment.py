"""
Filename: Theme Park Program for Staff Use
Author: Sam Booth
Date: 28/06/2022
Description: Program for staff at the theme park to use to find the entrance
             price for visitors and the rides they are allowed to use.
"""

#Set lists - entrance levels, rides
rides = ["Hakuna Matata", "A Walk in the Park",
         "The Bulldog", "Mr Rager", "Hell's Kitchen", "Kilamanjaro",
         "Stampede", "The Drop", "Don't Look Down", "Bronco"]
height_restrictions = [80, 80, 110, 120, 120, 120, 150, 150, 150, 160]
entrance_levels = ["red", "pink", "green", "yellow"]

group_level_validation = False
group_members_validation = False
person_height_validation = False

#Print entrance levels, ask what level of entrance the group is
#Validate this
print(""""The available entrance levels are {}
The higher entrance levels(more letters) have more perks.
These include a higher chance to skip to the front of the queue
and free ice creams!!""".format(entrance_levels))


while not group_level_validation:
    group_level = input("Enter group entrance level ")
    if group_level.lower().strip() in entrance_levels:
        group_level_validation = True
    else:
        print("Please enter a valid entrance level ")

#Ask how many members there are in the group and validate this
while not group_members_validation:
    try:
        group_members = int(input("Enter number of members in the group "))
        group_members_validation = True
    except ValueError:
        print("Please enter a number of group members ")

#Ask the names and heights(cm) of each member in the group
#Work out which rides each member is able use by which requirements they meet
#Requirements - height
for index in range(group_members):
    person_name = input("What is the name of person {} ".format(index+1))

    while not person_height_validation:
        try:
            person_height = int(input("What is the height of {} in cm ".format(person_name)))
            person_height_validation = True
        except ValueError:
            print("Please enter a number of centimetres")
    person_height_validation = False

    rides_available = 0

    for index1 in range(0,9):
        if person_height > height_restrictions[index1]:
            rides_available = rides_available+1
    print("{} can use the rides: {}".format(person_name, rides[0:rides_available]))
    print()

#Work out price based on $5 for each person times len of the entrance level
group_price = len(group_level.strip())*5*group_members

#Print total price of group entrance
print("The price for your group is ${}".format(group_price))
