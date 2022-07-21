import logging
import re


"""###########************CLASS FILES **************############"""
class Position:
    def __init__(self, description, name) -> None:
        self.description = description
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.lst = []
        self.name=str(name)

class Player:
    def __init__(self, name,lst=None) -> None:
        self.name = str(name)
        if lst is None:
            lst=[]

    def __str__(self):
        return "Name: " + self._name + ", list: " + lst


"""class Gamer(Position):
    def __init__(self,name,location):
        self.name=name
        self.location=location"""

"""###########************ ROOM POSITION OBJECTS  **************############"""

Front_Door = Position("You are at FRONT-DOOR\nDoors are to your : [NORTH, WEST,EAST]", "FrontDoor")
Dining_Room = Position("You are at the DINING-ROOM\nDoors are to your : [NORTH,WEST]", "DiningRoom")
Kitchen = Position("You are in the KITCHEN\nDoors are to your : [NORTH,SOUTH, WEST,]", "Kitchen")
Stairs=Position("You are at the STAIRS\nDoors are to your : [SOUTH, WEST,EAST]", "Stairs")
Sitting_Room=Position("You are at the SITTING-ROOM\nDoors are to your : [NORTH,SOUTH,EAST]", "SittingRoom")
Patio=Position("You are at the patio\nDoors are to your : [SOUTH,EAST]", "Patio")
Bed_room=Position("You are in the  Bedroom\nDoors are to your : [NORTH,EAST]", "Bed_room")
Exit = Position("You have gotten to the exit\n", "Exit")

"""###########************ ROOM POSITION EXITS  **************############"""

Front_Door.north = Stairs
Front_Door.south = Front_Door
Front_Door.east = Dining_Room
Front_Door.west = Bed_room

Bed_room.north = Sitting_Room
Bed_room.south = Bed_room
Bed_room.east = Front_Door
Bed_room.west = Bed_room

Dining_Room.north = Kitchen
Dining_Room.south = Dining_Room
Dining_Room.east = Dining_Room
Dining_Room.west = Front_Door

Kitchen.north = Exit
Kitchen.south = Dining_Room
Kitchen.east = Kitchen
Kitchen.west = Stairs

Stairs.north = Stairs
Stairs.south = Dining_Room
Stairs.east = Kitchen
Stairs.west = Sitting_Room

Sitting_Room.north = Patio
Sitting_Room.south = Bed_room
Sitting_Room.east = Stairs
Sitting_Room.west = Sitting_Room

Patio.north = Patio
Patio.south = Sitting_Room
Patio.east = Exit
Patio.west = Patio


"""###########************ STARTING  VARIABLES AND IMPORTS  **************############"""

"""def main():"""

logging.basicConfig(filename="TextBasedGame.log",level=logging.DEBUG,format='%(asctime)s :: %(message)s')


"""###########************ ROOM DIRECTION METHODS  **************############"""

def gone_north(name):
    print("You walked due North")
    restart = ()
    if location == Stairs:
        print(location.description)
    elif location == Kitchen:
        print(location.description)
    elif location == Sitting_Room:
        print(location.description)
    elif location == Patio:
        print(location.description)
    elif location== Exit:
        print("You won")
    else:
        restart = ('y')
        print("NO EXIT HERE ")



def gone_south(name):
    print("You walked due South")
    restart = ()
    if location == Dining_Room:
        print(location.description)
    elif location == Kitchen:
        print(location.description)
    elif location == Front_Door:
        print(location.description)
    elif location == Bed_room:
        print(location.description)
    elif location == Sitting_Room:
        print(location.description)
    else:
        restart = ('y')
        print("NO EXIT HERE ")


def gone_east(name):
    print("You walked due East")
    restart = ()
    if location == Dining_Room:
        print(location.description)
    elif location == Front_Door:
        print(location.description)
    elif location == Bed_room:
        print(location.description)
    elif location == Kitchen:
        print(location.description)
    elif location == Stairs:
        print(location.description)
    elif location == Exit:
        print(location.description)
    else:
        restart = ('y')
        print("NO EXIT HERE ")


def gone_west(name):
    print("You walked due West")
    restart=()
    if location == Bed_room:
        print(location.description)
    elif location == Front_Door:
        print(location.description)
    elif location == Sitting_Room:
        print(location.description)
    elif location == Stairs:
        print(location.description)
    else:
        restart=('y')
        print("NO EXIT HERE ")


"""#####*****POSITION METHODS******#########"""

print("WELCOME TO THE ESCAPE ROOM GAME \nYour aim is to locate the Exit \n")
print("*******GAME STARTS********\n")

#Creating the plaer object
lst=[]
while True :
    try:
        P1 = Player(input("Player Enter Yout Name >>>>>>   :  \n"),lst)
        mat = re.match("^[0-9 ]+$", P1.name)
        if mat != None:
            raise ValueError
    except ValueError as ve:
        print("Player name cant be an Integer")
    else:
        break
lst.append(P1.name)


fname="playerDetails.csv"
"""def savePlayerDetail(fname,players_History):
    with open(fname,"a") as f:
        for elem in players_History:
            #print(elem)
            f.write("Player Name: "+P1.name+"Last Location: "+location.name)"""
location = Front_Door


location_coordinates = ["north", "east", "west", "south", "quit"]
location_list_string =",".join(map(str, location_coordinates))


def loadplayerDetail(fname):# check if the player exited previously , and get last location
    players_History=[]

    with open(fname,"r") as f:
        for line in f:
            info =line.split(",")
            if info[0]== P1.name:
                last_location=info[-1]
                print("You are loading from file......... \nYour last location was: ",last_location)
                if (last_location=="Stairs"):
                    location=Stairs
                elif last_location =='SittingRoom':
                    location=Sitting_Room
                elif last_location == 'Bedroom':
                    location =Bed_room
                elif last_location =='DiningRoom':
                    location=Dining_Room
                elif last_location == 'Patio':
                    location =Patio
                elif last_location == "Kitchen":
                    print("this class kitchen")
                    location= Kitchen
                else:
                    location= Front_Door
                    print("Game Already completed\nRestarting Game From Front_Door.....")
            else:
                location =Front_Door

            return location


"""#####*****GAME STARTS******#########"""


location=loadplayerDetail(fname)
#location=loadplayerDetail(fname)
user_input = " "
while user_input != "quit":
    #loadplayerDetail(fname)
    #savePlayerDetail(fname, lst)
    lst.append(location.name)
    if location == Exit:
        print(P1.name,": You have gotten to the Exit in ",len(lst)-2,"moves")
        logging.info(P1.name+" WINS")
        break

    print("Enter input in the format  : ",location_coordinates)
    general_input = (str(input(P1.name+" you are at :" + location.name + " Go where next >>>\n?")))
    user_input=general_input.lower()
    if user_input not in location_coordinates:
        print("Wrong direction entered \n Enter input in this format : ",location_coordinates)
    logging.info(P1.name+ " moved in " +user_input + " direction from " +location.name+" \n")


    if user_input == 'north':
        locator= location
        location = location.north
        gone_north(location.name)
        if locator==location:
            print("NO EXIT IN NORTH DIRECTION FROM THIS ROOM,PLEASE TAKE ANOTHER EXIT")
            logging.info(P1.name + " tried to move NORTH but no exit in this direction")

    elif user_input == 'south':
        locator = location
        location = location.south
        gone_south(location.name)
        if locator==location:
            print("NO EXIT IN SOUTH DIRECTION FROM THIS ROOM,PLEASE TAKE ANOTHER EXIT")
            logging.info(P1.name + " tried to move SOUTH but no exit in this direction")

    elif user_input == 'east':
        locator = location
        location = location.east
        gone_east(location.name)
        if locator==location:
            print("NO EXIT IN EAST DIRECTION FROM THIS ROOM,PLEASE TAKE ANOTHER EXIT")
            logging.info(P1.name+" tried to move EAST but no exit in this direction")

    elif user_input == 'west':
        locator = location
        location = location.west
        gone_west(location.name)
        if locator==location:
            print("NO EXIT IN WEST DIRECTION FROM THIS ROOM,PLEASE TAKE ANOTHER EXIT")
            logging.info(P1.name + " tried to move WEST but no exit in this direction")

    elif user_input =='quit':
        print(P1.name," has QUIT")
        logging.info("The user quits the game from the " + location.name + " position")
        break

    """else:
        print("Command not recognised")
        print("Please Enter direction in the format: "+location_list_string)
        logging.info(player_name+" entered a location: "+user_input + "which is not part of the 4 coordinated ")
        print("Your New location is ", location.name)"""

#print(lst)
print(P1.name," Your Route is as follows ")
for i in range(1,len(lst)):
    print(lst[i])

stringList =",".join(map(str, lst))
"""To make a string of the list array to append to the file"""
#print("The string List: ", stringList)

fname="playerDetails.csv"
def savePlayerDetail(fname,lst):
    with open(fname,"a") as f :
        #for elem in lst:
        """f.write("Player Name: "+P1.name+"Last Location: "+location.name)"""
        f.write(lst)
        f.write("\n")
        print("Your Route has been saved to file ")
        logging.info("Saving Player Details to file...")

savePlayerDetail(fname, stringList)


"""if __name__ =="__main__":
    main()"""

