# ben simms is a kook
import readline
import math
import random
import time
# Welcome to APBP! bruh.
# We will rule the world.

print("""
+---------++       +------------+       ++-------------+         +-----------+
|         |        |            |        |             |         |           |
|         |        |            |        |             |         |           |
|         |        |            |        |             |         |           |
|         |        +------------+        +------------++         +-----------+
+---------+        |                     |            |          |
|         |        |                     |            |          |
|         |        |                     |            |          |
|         |        |                     |            |          |
+         +        +                     +------------++         +
""") #There we go. 

def armorfxn(item): #Chances for certain armor, describes the amount of health that is protected from certain armor.
    num = 0
    bbn = []
    while num <= 3:
        if item[num] == 0:
            bbn.insert(num, "no")
        elif item[num] == 5:
            bbn.insert(num, "cardboard")
        elif item[num] == 10:
            bbn.insert(num, "leather")
        elif item[num] == 15:
            bbn.insert(num, "bronze")
        elif item[num] == 20:
            bbn.insert(num, "iron")
        elif item[num] == 25:
            bbn.insert(num, "chainmail")
        num += 1    
    return bbn

#### This is the main global variable setup we have here.  ###
class setup():  # chest config[0:4]: 0 = Nothing 1 = AP , 2 = sword, 3 = shotgun, 4 =  pistol # Monsters = 
    def __init__(self):
    # Global and important variables
        self.bossposition = ([(random.randint(5, 10) * random.choice([-1,1]) ), random.randint(-1, 1), ( random.randint(5, 10) * random.choice([-1,1]) ) ])
        self.player_health = 200
        self.inCombat = False
        self.roomposition = [ 0 , 0 , 0 ] # x, y, z
        self.chestconfig = [10, 2, 1, 1, 2, 1] # same as inventory
        self.chestnames = ["1 sword", "2 bullets", "1 shotgun", "1 pistol", "2 shotgun shells", "1 AP"]
        self.monsterconfig = [[30, 40, 50, 60, 70], [15, 23, 30, 38, 45], [70, 90, 110, 130, 150]] # chance, damage, health
        self.rooms = [[[0 , 0 , 0 ], False , False, None, [0, 0]]] # coords, chest, monster, fallenitems, chestinv
        self.inventory = [10, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0] # 0 = sword, 1 = bullets 2 = shotgun 3 = pistol 4 = shells 5 = ap 6 = keys 7 = compass 8 = helmet 9 = torso 10 = pants 11 = boots
        self.monsters = [[0, 0, 0]]
        self.exit = False
        self.fallenitems = []
        self.defense = (int(self.inventory[8] + self.inventory[9] + self.inventory[10] + self.inventory[11])/100) 
        self.armorr = ["no", "cardboard", "leather", "bronze", "iron", "chainmail"]
        self.armor3 = ["helmet", "torso", "pants", "boots"]
        self.armor = [self.inventory[8], self.inventory[9], self.inventory[10], self.inventory[11]]
        self.armor2 = armorfxn(self.armor)
        


z1 = setup() # Makes it easier to access in the program.
z1.rooms.append([z1.bossposition, False, True]) # Sets up the boss level

def reset_def(): # This resets the inventory at the beginning of the game and also whenever you call upon it.
    z1.armor = [z1.inventory[8], z1.inventory[9], z1.inventory[10], z1.inventory[11]]
    z1.armor2 = armorfxn(z1.armor)
    z1.defense = (int(z1.inventory[8] + z1.inventory[9] + z1.inventory[10] + z1.inventory[11])/100)

# 0 = sword, 1 = bullets 2 = shotgun 3 = pistol 4 = shells 5 = ap 6 = keys 7 = compass 8 = helmet 9 = torso 10 = pants 11 = boots
def chestgen(): # This is the main code for the chest generation program. There are different items that the chests give to the player ( it gives two items from this list below)
    num = 0
    n = random.randint(8, 11)
    chestlist = [[250, [5, random.randint(1, 2)], " AP"], [375, [n, 5-z1.inventory[n]], " 1 cardboard " + z1.armor3[n-8]], [438, [n, 10-z1.inventory[n]], " 1 leather  " + z1.armor3[n-8]], 
    [470, [n, 15-z1.inventory[n]], " 1 bronze  " + z1.armor3[n-8]], [490, [n, 20-z1.inventory[n]], " 1 iron " + z1.armor3[n-8]], [500, [n, 25-z1.inventory[n]], " 1 chainmail " + z1.armor3[n-8]], 
    [625, [0, 1], " sword"], [688, [3, 1], " pistol"], [750, [2, 1], " shotgun"], [875, [1, random.randint(1, 10)], " bullets"], [1000, [4, random.randint(2, 5)], " shotgun shells"] ]
    a = random.randint(0, 999)
    while True:
        if a < chestlist[num][0]:
            b = chestlist[num][1]
            if a < 500 and a > 249:
                c = chestlist[num][2]
            else:
                c = str(chestlist[num][1][1]) + chestlist[num][2]
            break
        else:
            num += 1
    if b[1] > 0:
        return[b, c]
    else:
        return None
        
def chestgen1(): # when you open a chest it randomly gives you certain items
    a = 1
    while a != None:
        n = chestgen()
        if n == None:
            pass
        else:
            return n
### made before the whole donald trump president thing.... :p
# Drawn by me :D Donald Trump Face *it is our trump card*
trump = """
                                           XXXXXXXXX XX
                           XX X XX X XX XXXX       XX  XXX XXXXX XXXXX
                     X XXX    X    XX       X       XX       XX       XXXXXX
                XXXXX  XXX    XX    XX      XX       XX        XX          XXXX
             XXX         XX     XX    X       X        X          XX        XX XXXXX
            XX  XX         XX    XX    XX       X        X          X        XX    XX
         XXX       XX        X     X      X       X        X          X X     XXX    XX
       XXX           X X      XX   XX      X       X         X X         XXXX   XXXXXXXXXX
      XX              XX  X    X      X     XXXX    X            XX          XXXXXXXXXXXXXX
     XX                X    X X XXX    X        XXX XXX     XX     XXX XXXXXXXXXX          X
     X                XX        X  XXX  X X          XXXXXXXX   X XXXXX    XX              X                    
    X               XX           XXX XX    XX X         X XXXXXX             XX            X        
   XX              X                XX XX      XX X      XXX                  XX            X       
   X           XXX                    XX XX         XXX X                      XX           X       
   X         XXX                       XXX XX  XX XX   XX                       X                 
  X           X                          XXXXXX                                  X          X       
 XXX          X                          XX                                      X                 
   XXX        X                                                                   X         X       
   XX          X                                              XXX                 XX                
   X           X              X XXXX                         XX XXXXXXXXXXX        X       X                       
   X           X      XXXXXXXXXXX  XX                        X             XX      X       X
  XX          XX          X         X                        XXXX X X XX            X
  X           X     XXX XX X  X  X X X XXXX             XXXXX      XXXX XXXX        X      X                   
  X           X    X            XXXXXXXX   XXX         XX X    XXXXXXXX     X       X      X                 
  X           X    XXXXXXXXX     XX XXX      X            XXXXXXXX    X     X        X     X            
  X          XX             XXXXXXXXXXXX XXXXX                   XXXX                X     X           
   X         X                           XXX                                         X     X          
   X        XX                         XX                                            XXXXXXX             
   X        X                                                                              XXXXX       
   XX      XX                                                                                  XX      
  XXX      XX                            XXX XXX         XXXX                          X        X           
 XX         X                            X  XX  X    XXX   XX                          XXXX      X
XX          X                             XXX   X      XX XX                              XXX    X
X           X                                                                             XXX  XXX
X           X                                                                        XXXXXXXXXXX
XX          X                                                                    XXXXX XXX   X
 XX         X                            XXXXXXXXXXXX XX                         XX          XX
  XX        X                       XXXXXX               XX XXXXXX               X            X
    XXXX    X                       X     XXXXXXXXXXXXXXXXX      XX              X            XX                               X
       XX   XX                                                                   X             XX
        X    XXXX                                                                 X             X
        X      XXX                                                               XXX            XX
        X     XX  XX                                                             X  X     X       XXX
        XX  XXX    XXXX            XXX                                           X  XXXXXXXX    XXXX
         XXXX         XXXX XXXXXXXXX XX            XXXX                        XXX          XXXX
                         XXX          XXXXXX XXXXXX   XXXXXXXXX           XXXXXX
                                        XX XXX                XXXXXXXXXXXXX
                                       
               
"""

def open_chest(): # Basic display when opening a certain chest. 
    a = chestgen1()
    z1.inventory[a[0][0]] += a[0][1]
    reset_def()
    print("You have received " + a[1] + " from the chest!")

class database(): # This is the help command database that we draw certain info from. not super necesary but fun.
    helpgame = ["help", "command", "help: gives info on a certain command or argument(item in game, direction of motion, etc.)", ""]
    use = ["use", "command", "use: attempts to use selected item or object\nSubcommands: sword, shotgun, key, pistol, compass", ""]
    move = ["move", "command", "move: moves in specified direction (north, south, east, west)", ""]
    east = ["east", "argument", "east: move east one room", ""]
    west = ["west", "argument", "west: move west one room", ""]
    north = ["north", "argument", "north: move north one room", ""]
    south = ["south", "argument", "south: move south one room", ""]
    AP = ["AP", "argument", "AP: Arnold Palmer. Drink of the Gods. Restores 25 health per use.", "drink"]
    health = ["health", "argument", "health: your total health. can be restored with certain items.", "attribute"]
    sword = ["sword", "argument", "sword: a rusty old iron sword. doesn't look like it will be very effective in combat, but its better than nothing.", "weapon"]
    shotgun = ["shotgun", "argument", "shotgun: a double barreled shotgun. looks pretty effective.", "weapon"]
    pistol = ["pistol", "argument", "pistol: a service issue m9 pistol. looks fairly good. holds 6 bullets per magazine.", "weapon"]
    compass = ["compass", "argument", "compass: tells distance from BEN SIMMS"]

x = database()

database_total = [x.helpgame, x.use, x.move, x.west, x.north, x.south, x.AP, x.health,
                    x.sword, x.shotgun, x.pistol, x.compass]
                    
row0 = [item[0] for item in database_total]


#Definition of functions in the thing
def addlists(list1, list2): # adds lists together for other programs we have around.  
    new_list =[]
    counter1 = 0
    while counter1 < len(list1) and counter1 < len(list2):
        new_list.append(int(list1[counter1]) + int(list2[counter1]))
        counter1 += 1
    return(new_list)
        

def isempty(listuno): # returns whether or not a given list is empty
    if len(listuno) == 0:
        return True
    else:
        return False

def indexmulti(val, list1): # This looks through multiple lists and returns items.  
    list2 = list1[:]
    new_vals = []
    while list2.count(val) > 0:
        new_vals.append(list2.index(val))
        temp_val = list2.index(val)
        list2.remove(val)
        list2.insert(temp_val, '0')
    return (new_vals)

def slicemulti(indexes, list3): # This slices lists into given indexes, I beleive there is a thing that comes w/ python that does it.
    list_new = []
    num1 = 0
    while num1 < len(indexes):
        list_new.append(list3[indexes[num1]])
        num1 = int(num1) + 1
    return list_new

def combatstatus(): # when run, gives the player their status in combat.
    print("You have " + str(z1.player_health) + " health, and the monster has " + str(z1.monsters[-1][2]) + " health.")


def mondead(): # Gives items in a chest when you kill a monster. post combat function basicallly.
    if z1.monsters[-1][2] <= 0:
        z1.rooms[room_number()][2] = False
        z1.inCombat = False
        print("You have slain the monster and recieved a chest key!")
        z1.inventory[6] += 1
        a = random.randint(0, 3)
        if a == 0:
            changehealth(50)
            print("You have won the dice roll and have gained 50 health!")
        else:
            print("You lost the dice roll and did not gain 50 health.")
        if z1.rooms[1][2] == False: #once you beat the boss the game is boring, but you can go and defeat all the other monsters, this allows for our game to be easily edited for more editions.
            print(trump)
            print("You have defeated the boss! You win! You may continue wandering the dungeons at your leisure.")
        return True
    else:
        return False
        
def changehealth(input2): # Changes a players health.  
    z1.player_health += input2
    if z1.player_health > 200:
        z1.player_health = 200

def helpgame(input1): # More help function
    if input1 == "EMPTY":
        print("Main Commands: use, move, inspect, exit\nUse 'help (subcommand)' for more info")
    else:    
        print(database_total[row0.index(input1)][2])

def use(item, on, directobject): # The main function of our program. Lets the user use items.
    if item == "sword" or item == "pistol" or item == "hands" or item == "shotgun": # combat items, options
        if directobject == "self" or directobject == "myself":
            attack_monster = False
            act_on_self = True
        else:
            attack_monster = True
            act_on_self = False
    else:
        attack_monster = False
        act_on_self = False
    
                
    if item == "sword": #Gives different chances and damage info for each of the items, not very concise but it works.
        chance = 75
        damage = 40
        dist = 6
        if z1.inventory[0] > 0:
            ammo = True
        else:
            ammo = False
    elif item == "pistol":
        chance = 65
        damage = 100
        dist = 7
        if z1.inventory[1] > 0 and z1.inventory[3] > 0:
            ammo = True
            z1.inventory[1] = z1.inventory[1] - 1
        else:
            ammo = False
    elif item == "shotgun":
        chance = 100
        damage = 75
        dist = 7
        if z1.inventory[4] > 0 and z1.inventory[2] > 0:
            ammo = True
            z1.inventory[4] = z1.inventory[4] - 1
        else:
            ammo = False
    elif item == "AP": # Gives variant health to a player from AP
            if z1.inventory[5] > 0:
                ap = random.choice([["homemade", 100], ["arizona", 75], ["snapple", 50], ["jank", 25]])
                changehealth(ap[1])
                print("You chugged some " + ap[0] + " AP and gained " + str(ap[1]) + " health! #khaked")
                z1.inventory[5] -= 1
            else:
                print("You don't have enough AP you fool")
    elif item == "hands": # You can fight the monster with your hands if you don't have anything. Not suggested.
        damage = 5
        chance = 50
        dist = 1
        ammo = True
    else:
        damage = 0
        chance = 0
        dist = 0
        ammo = True
    if z1.inCombat == True: # options for when a player is "in combat"
        n2 = True
        n3 = mondead()
        while n3 == False and n2 == True:
            rng_player_damage = int(random.gauss(damage, dist))
            rng_monster_damage = round(((1-z1.defense)*int(random.gauss(z1.monsters[-1][1], 3))))
            if attack_monster == True: # Attacks a monster
                if ammo == False:
                    print("This weapon is all used up!")
                elif random.randint(0, 100) <= chance:
                    z1.monsters[-1][2] -= rng_player_damage
                    print("You did " + str(rng_player_damage) + " damage!")
                else:
                    print("You missed")
            elif act_on_self == True: # kills yourself (mostly for testing)
                if ammo == False:
                    print("You do not have enough ammo!")
                elif random.randint(0, 100) <= chance:
                    changehealth(-rng_player_damage)
                    print("You did " + str(rng_player_damage) + " damage! The original value was " + str(rng_player_damage) + " but you blocked " + str((z1.defense)*(rng_player_damage)) + " damage!")
                else:
                    print("You missed")
            else: # if you aren't lucky, you can miss the monster fully.
                print("you did nothing. get RKO'ed")
            
            n3 = mondead() # This explains how much damage the monster does and howm much your armor helps.
            if z1.monsters[-1][2] > 0:
                time.sleep(.5)
                if random.randint(0, 100) <= z1.monsters[-1][0]:
                    changehealth(-rng_monster_damage)
                    print("The monster did " + str(rng_monster_damage) + " damage! The original value was " + str(rng_monster_damage + (round(rng_monster_damage/(1-z1.defense))*z1.defense)) + " but you blocked " + str(round(rng_monster_damage/(1-z1.defense))*z1.defense) + " damage!")
                else:
                    print("The monster missed!")
                n2 = False
    else: 
        if act_on_self == True:
            rng_player_damage = int(random.gauss(damage, dist))
            if ammo == False:
                print("You do not have enough ammo!")
            elif random.randint(0, 100) <= chance:
                changehealth(-rng_player_damage)
                print("You did " + str(rng_player_damage) + " damage! The original value was " + str(rng_player_damage) + " but you blocked " + str((z1.defense)*(rng_player_damage)) + " damage!")
            else:
                print("You missed")
        elif item == "compass": # Shows how far away you are from the boss room with a little twist ;)
            print("You are about " + str(int(math.pow(int(math.pow(abs(z1.roomposition[0] - z1.bossposition[0]), 2) + math.pow(abs(z1.roomposition[2] - z1.bossposition[2]), 2)), .5))) + " rooms away from the boss.")
            try:
                print("You are about " + str(int(math.pow(int(math.pow(abs(z1.roomposition[0] - z1.rooms[(item[3] for item in z1.rooms).index(True)][0][0]), 2) + math.pow(abs(z1.roomposition[2] - z1.rooms[(item[3] for item in z1.rooms).index(True)][0][0]), 2)), .5))) + " rooms away from your fallen inventory.")
            except:
                pass
        elif item == "key" and directobject == "chest" and ( z1.rooms[room_number()][1] ): # opens the chest. gives peopel things if they have keys.
            if z1.inventory[6] > 0:
                z1.inventory[6] -= 1
                open_chest()
                open_chest()
                z1.rooms[room_number()][1] = False
            else:
                print("You don't have enough keys! Kill monsters!")


# Gives information on a given subject.
def inspect(object1): #unnecessary when we have to still make things work.
    if object1 == "monster" or object1 == "boss" or object1 == "ben simms":
        if z1.monsters[-1][0] > 0:
            return("The monster has " + str(z1.monsters[-1][2]) + " health, a " + str(z1.monsters[-1][0]) + " percent chance to hit, and does " + str(z1.monsters[-1][1]) + " damage per successful hit.")
        else:
            print("There is no monster here!")
    elif object1 == "self":
        return("You have " + str(z1.player_health) + " health! Your current defense value is " + str(z1.defense*100) + ". You are wearing " + z1.armor2[0] + " helmet, " + z1.armor2[1] + " breastplate, " + z1.armor2[2] + " pants, " + z1.armor2[3] + " boots.")
    elif object1 == "door":
        return("There are four rusty doors around you, one in each direction.")
    elif object1 == "inventory":
        return("In your inventory you have " + str(int(int(z1.inventory[0]/10 - .1) + 1)) + " swords, " + str(z1.inventory[1]) + " bullets, " + str(z1.inventory[2]) + " shotguns, " + str(z1.inventory[3]) + " pistols, " + str(z1.inventory[4]) + " shells, " + str(z1.inventory[5]) + " APs, " + str(z1.inventory[6]) + " keys and " + str(z1.inventory[7]) + " compass.")
    elif object1 == "room":
        fff = []
        if z1.rooms[room_number()][2]:
            fff.append("a monster")
        if z1.rooms[room_number()][1]:
            fff.append("a chest")
        if isempty(fff):
            fff.append("nothing")
        return("you are in " + str(z1.rooms[room_number()][0]) + " with " + " and ".join(fff) + " in it.")

# Tells us what number room the player is in from the database of rooms
def room_number(): 
    counter = 0
    while counter != (len(z1.rooms)):
        if z1.rooms[counter][0] == z1.roomposition:
            return(counter)
        counter += 1
    return(None)

#This changes the postiton of the room.  And creates a new room if needed.
def changeposition(x,y,z): 
    z1.roomposition = [ ( z1.roomposition[0] + x ) , ( z1.roomposition[1] + y ) , ( z1.roomposition[2] + z ) ] 
    if room_number() == None:
        z1.rooms.append([z1.roomposition, random.choice([False, True]), random.choice([False, True]), None, False])
    print("You have changed rooms. Now, " + inspect("room"))
    if z1.rooms[1][0] == z1.roomposition:
        print("You have entered the boss battle!")
    if z1.rooms[room_number()][3]:
        print("You have reacquired the items you dropped on death!")
        z1.inventory = addlists(z1.inventory, z1.fallenitems)
        z1.fallenitems = []
        z1.rooms[room_number()][3] = False
    if z1.rooms[room_number()][2]:
        if input("Do you want to fight? ").lower() == "yes":
            print("Welcome to combat! Type 'use [weapon] on monster' to attack! But be careful, monsters are dangerous.")
            z1.inCombat = True
            if z1.roomposition == z1.bossposition:
                z1.monsters.append([70, 50, 500])
            else:
                z1.monsters.append([z1.monsterconfig[0][random.randint(0, 4)], z1.monsterconfig[1][random.randint(0, 4)], z1.monsterconfig[2][random.randint(0, 4)]]) 
        else:
            z1.inCombat = False
            z1.roomposition = [ ( z1.roomposition[0] - x ) , ( z1.roomposition[1] - y ) , ( z1.roomposition[2] - z ) ]
            print("You have gone back to your previous room")

# Moves the player between rooms.
def move(direction):
    if direction == "east":
        changeposition(1,0,0)
    elif direction == "west":
        changeposition(-1,0,0)
    elif direction == "north":
        changeposition(0,0,1)
    elif direction == "south":
        changeposition(0,0,-1)
    elif direction == "up":
        if z1.roomposition[0] == 0 and z1.roomposition[2] == 0:
            changeposition(0,1,0)
        else:
            print("You cannot move up. Go to the home room w/ the stairs")
    elif direction == "down":
        if z1.roomposition[0] == 0 and z1.roomposition[2] == 0:
            changeposition(0,-1,0)
        else:
            print("You cannot move down. Go to the home room w/ the stairs")
    else:
        print("Unknown move command, Use'move north/south/east/west/up/down' to move.")

# Is the main movement of the program

def rungame(): # This is the function that runs the commands if you are alive.  
    if z1.inCombat:
        print("It is your turn!")
        combatstatus()
    userinput = input("> ")
    user_input = userinput.split()
    cmd = user_input[0]
    args = user_input[1:int(len(user_input))]
    while isempty(user_input) == False:
        if isempty(args):
            args = ["EMPTY"]
        if cmd == "help":
            helpgame(args[0])
        elif cmd == "move":
            if not z1.inCombat:
                move(args[0])
            else:
                print("You can't flee from Combat!")
        elif cmd in ["east", "west", "north", "south"]:
            if not z1.inCombat:
                move(cmd)
            else:
                print("You can't flee from Combat!")
        elif cmd == "open" and args[0] == "chest":
            use("key", "on", "chest")
        elif cmd == "health":
            print("Your health is " + z1.player_health )
        elif cmd == "use":
            if len(args) == 1:
                args.append(0)
                args.append(0)
            use(args[0], args[1], args[2])
        elif cmd == "inspect":
            print(inspect(args[0]))
        elif cmd == "trump":
            print(trump)
        elif cmd == "inventory":
            inspect(cmd)
        elif cmd == "exit" or cmd == "suicide":
            if cmd == "exit":
                z1.exit = True
            z1.player_health = 0
        else:
            print("Unknown command. Use 'help' for a list of commands")
        user_input = []
reset_def() 
print("Welcome to the most kookie of the APBP games\nYou are in the home room. - Start by moving around with command 'move'\nUse 'help' if you need help\nThe goal is to find the boss level and slay\nUse your compass to find the boss 'use compass'")
print("Here are some basic tips: use the move command to move between rooms, ie move east, move west, etc.\nby using the inspect command, you can take a look at things such as your inventory, health, and armor values.")
while True:
    if z1.player_health > 0:
        try:
            rungame()
        except:
            print("Error!")
    elif z1.exit:
        break
    else:
        print("You died!") # if you die you have options to respawn or to exit the game.  
        if input("Do you want to respawn? ").lower() == "yes":
            z1.rooms[room_number()][3] = z1.inventory
            z1.player_health = 200
            z1.fallenitems = z1.inventory
            z1.inventory = [0, 0, 0, 0, 0, 0, 0, 1]
            z1.inCombat = False
            changeposition(-z1.roomposition[0], -z1.roomposition[1], -z1.roomposition[2])
        else:
            print("Thank you for playing!")
            break