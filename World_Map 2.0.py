# -*- coding: utf-8 -*-
import random
import sys

node = None  #variable that will later tell you where you start the game
unlock_room  = False  #variable that will be used to tell if you win the game or not. It it is true later, then you win, if it is still false, you loose. 
dead = False #possible death variable in Russian Roulette. 
Win = False

#Hangman Minigame
def hangman():
    print "You must play a game of hangman and win, and then continue to win the Amazing Race."
    print
    
    allwords = "mouse", "laptop", "espanol", "fire", "mr", "ms", "mrs", "test", "taking", "take", "tips", "congruent", "protractor", "step", "steps", "signs", "sign", "exit", "enter", "not", "who", "you", "are", "that", "gaming", "question", "questions", "holds", "you", "back", "think", "thought", "games", "game", "fabric", "cloth", "screw", "nail", "hammer", "squirt", "picture", "frame", "pictureframe", "for", "it", "is", "tape", "box", "phone", "cellphone", "user", "username", "password", "pass", "ruler", "measure", "comfortable", "the", "a", "alright", "day", "days", "bench", "brick", "bricks", "earaser", "pad", "panel", "tempeture", "blackborad", "chalk", "cube", "statue", "january", "febuary", "march", "april", "may", "june", "july", "august", "october", "november", "december", "month", "months", "ice", "door", "drawing", "liberty", "well", "good", "qiuz", "objective", "geometry", "math", "english", "spanish", "video", "food", "case", "water", "soda", "pyramid", "overhead", "projector", "umbrella", "textbook", "text", "bookcase", "tacos", "burritos", "wiebe", "kyle", "volume", "control", "error", "whipe", "pen", "trash", "gear", "clock", "stool", "chair", "desk", "grease", "bread", "motor", "marker", "monitor", "wire", "input", "fit", "cane", "stack", "weed", "drugs", "printer", "back", "whiteboard", "wood", "metal", "code", "Bible", "binder", "paper", "hilighter", "pencil", "bucket", "round", "circular", "hangman", "bottle", "nag", "expo", "green", "all", "word", "cabinet", "banner", "turtle", "mouse", "jellyfish", "peanuts", "whale", "tiger", "panther", "couger", "words", "flag", "chair", "triangle", "circle", "square", "trapaziod", "hexagon", "blue", "orange", "purple", "brown", "black", "white", "red", "moroon", "gold", "silver", "bronze", "medallion", "medal", "book", "movie", "trip", "car", "bike", "trike", "tricycle", "moped", "I", "ice", "idea", "ideal", "identical", "identification", "identify",  "bye", "hi", "if", "ignore", "ill", "illegal", "illness", "illustrate", "image", "imaginary", "imagination", "imaginative", "imagine", "imitate", "immediate", "immigrant", "immoral", "impact", "impatience", "impatient", "import", "stuff", "all", "cool", "nice", "zero", "zone", "zoo", "dog", "cat", "chat", "illuminati", "computer", "hello", "yard", "yawn", "year", "yearly", "yell", "yellow", "yes", "yesterday", "yet", "you", "young", "your", "yours", "yourself", "loooooser", "winner", "alligator", "llama", "comotellamas", "supercalifragilisticexpialidocious", "table", "tactful", "tactless", "tail", "take", "takeoff", "talent", "talk", "tall", "tank", "tap", "tape", "target", "task", "taste", "tax", "taxi", "tea", "teach", "teacher", "team", "teammate", "tear", "technical", "technique" #this is the list of possible words
    bank = random.choice(allwords)  #this chooses a random word from the "allwords"
    guesses = ""                    #this is an empyty list that adds every guess you guessed to it
    turns = 5                       #this is varaible that is how many turns to get to play hangman. 
    global unlock_room
    

    while turns > 0:                #while you still have turns left...
        wrong = 0                   #you have 0 wrong guesses. (No letters left to guess)
        for char in bank:          #for every character in the bank
            if char in guesses:    #if the character is part of the guesses...
                print char,        #then it prints the character you guesses in place of the underscore...
            else:                  #otherwise....
                print "_",         #it prints an underscore
                wrong += 1          #and your wrong goes up one. 
        if wrong == 0:             #if you have no wrongs(no letters left to guess)...
            print ""               
            print "You Won!"       #it'll print that you won
            unlock_room = True
            print ""               
            break
    
        guess = raw_input("Guess a letter: ")  #this is actually where you guess a letter
        guesses += guess             #and it adds it to the guess list
    
        if guess not in bank:       #if your guess is not in the bank then it ...
            turns -= 1               #takes one turn away
            print ""
            print "Wrong Letter"    #and tells you it was wrong
            print ""                #this is a blank line
            print "You have", turns, "turns left!"   #and it tells you how many turns you have left. 
            print ""                #this is a blank line
        
    if turns == 0:                   #if you used all your turns 
        print "Ha Ha, You lost!"     #it prints that you lost
        print "The word was", bank  #and tells you what the word was
        print ""                    #this is a blank line

#Russian Roulette Minigame                                
def RR():
    global dead                                              
    fullgun = "barrel 1", "barrel 2", "barrel 3", "barrel 4", "barrel 5", "barrel 6"
    chosen = random.choice(fullgun)    #randon barrel  -  what you got
    bulletIn = random.choice(fullgun)  #random barrel  -  where bullet is
    message = "You walk further into the alley. A man comes up to you and says that he wants you dead, but he will give you a chance of freedom. You must win in a game of Russian Roulette."
    
    print message  #prints above message which introduces the situation
    print
    print "Prepare yourself."
    print
    print "You raise the gun to your head. Dum Dum DUM!!!!!! YOU CLICK IT...!!!"  #suspence
    if bulletIn == chosen:
        print "Sorry. You got shot. You dead.  :("    #if they are the same you die, and the game ends.
        dead = True   #if you die, then dead will be true and you will exit the game. 
        raise SystemExit
    else:
        print "You got lucky this time. You can go free. You did not get shot.   :)"  #if not, you survive and continue on your way. 
                      
           

class Room:
    #Constructor
    def __init__(self, name, n_path, s_path, e_path, w_path, down_path, up_path, use_path, description):
        self.name = name
        self.description = description
        self.north = n_path
        self.south = s_path
        self.east = e_path
        self.west = w_path
        self.down = down_path
        self.up = up_path
        self.use = use_path
    #Movement Method
    def move(self, direction):
        global node
        node = globals()[getattr(self, direction)]

               
#ROOMS
             #Room Name                         #N    #S    #E    #W    #D    #U    #Use                                       #Description
Intro = Room('Introduction',                    None, None, None, None, None, None, 'Apartment',                               'Hello, and welcome to St. Petersburg, Russia. This is the last leg of the Amazing Race, with the grand prize of 1 million dollars. You and your partner must get to the end of the race before the other team does. To win you must press a buzzer hidden in a specific place. We will be near the buzzer to tell you where it is, but getting to the buzzer is a challenge in and of itself. You must complete the challenges given to you to go on. You will start in this random apartment in a random place in St. Petersburg. Good luck racers. *(Hint: Type "use" to go on. This will be a miscellanous direction/move.)*')
Apartment = Room('Apartment',                   None, None, 'Hall', None, None, None, None,                                    'You are in an apartment. It is a regular Russian apartment, complete with a complimentary vodka bottle. But sadly I think someone already drank it. There is a door to the east leading out of the room.')
Hall = Room('Hall',                             None, None, 'Lobby', 'Apartment', 'Lobby', None, hangman,                      'You are in a hall with a red carpet. It is on the second story. There is a stairway leading down on the far end of the hall. There is also an old man sitting at a small table next to a doorway. He is saying something to you in Russian. He appears to be calling you to him. The other team sees this as well. They walk to the old man. This must be one of the challenges needed to go on.                                                                                                   *(Hint: If you have already completed this challenge just continue on your way please. Thank you.)*')
Lobby = Room('Lobby',                           None, None, 'Outside', 'Hall', None, 'Hall', None,                             'You are in a lobby on the first story. There is a red carpet and the Russian flag on the wall. There is the door on the east leading to outside. You must hurry. The other team rushes past you out into the street. They must have finished Hang Man with the old man. You must hurry to beat them and win the ultimate prize.')
Outside = Room('Outside',                       None, 'Intersection', None, 'Lobby', None, None, 'Info_Center',                'You are just ouside of the apartment complex with your partner. You are on a sidewalk next to a street. You see a booth with the sign that says ’Info Center’. It has a map on it. It might help. There are also stores on the other side of the street. Such as ‘Russian Walmart’ and Russian ’El Polo Loco’. But you have no time to shop. You must go on.')
Info_Center = Room('Info Center',               None, 'Intersection', None, None, None, None, 'Outside',                       'You walk to the map on the Info Center. The map shows you that you are on the street ’Blackstone’. It goes north to south. The apartment complex was further north, and further south is an intersection where Blackstone and Ashlan meet. Ashlan goes west to east. But on the east is a dead end with abandoned buildings. On the west is the ’Church of the Savior on Blood’, the splendor of Russia. At the end of Blackstone, on the south is an alley.')
Intersection = Room('Intersection',             'Outside', 'Alley', 'Dead_End', 'Ashlan', None, None, None,                    'You are at the intersection of Blackstone and Ashlan. Back up north leads up Blackstone, south leads to an alley. To your east is a dead end with some abandoned buildings, and on the west is a row of houses, and then at the end is a large palace, which must be the ’Church of the Savior on Blood’.')
Dead_End = Room('Dead End',                     'Factory', 'House', None, 'Intersection', None, None, None,                    'You are in a dead end. To the north is an abandoned factory. To the south is an abandoned house. West goes back to the intersection.')
Factory = Room('Abandoned Factory',             None, 'Dead_End', None, None, None, None, None,                                'You are in an old abandoned factory. There are many old machines that once did something. Every step makes a creek. *BOOM!* A machine falls, revealing the other team behind it. They rush past you to the outside. You must hurry to get ahead and win.')
House = Room('Abandoned House',                 'Dead_End', None, None, None, None, None, None,                                'You are in an old abandoned house. It was once an old nice house. Now it looks like it hasn’t been lived in you many years. You walk into the family room, but the other team rushes past you, out to the street. They must have seen that there was nothing to find here. You and your partner must hurry to get past them and win!')
Alley = Room('Alley',                           'Intersection', None, None, None, None, None, RR,                              'You walk into an alley. You and your partner are scared. But what if the end is here? You must continue looking. But there could be danger. WAIT! What was that? You continue walking to find out.....')
Ashlan = Room('Ashlan',                         None, None, 'Intersection', 'Castle', None, None, None,                        'You are on the street Ashlan. There are houses on the south side. But you don’t have time to visit. You must keep looking. You walk down the street. Luck is not on your side. As you walk down the street, you trip on a wire, get attacked by a dog, and break a fence. It ok though because if you win, you can buy a million fences. You see the other team rush past you on the other side of the street to the ’Church of the Savior on Blood’.')
Castle = Room('Church of the Savior on Blood',  None, None, 'Ashlan', None, None, 'Top', None,                                 'You rush to the castle. There you see the hosts of the show. They are waiting for you. You and the other team reach the point at the same time. You all start arguing who was there first. But one of the hosts says to calm down. You quiet down. ‘The end of the race is not here. You must climb to the top of the highest sphere of this building to win. There is a buzzer at the top, and you must press it to win.’')
Top = Room('Top of the building',               None, None, None, None, 'Winner', None, 'Winner',                              'You rush to reach the top. You climb up the wall with your partner. But you have no climbing gear. The other team does however. There is a label still on a rope that says Walmart. Maybe shopping would have helped. But now it is too late. You must get up there faster than them. It is more unsafe for you, but you can go faster without the gear. You reach the bottom of the towers. The buzzer must be on the tallest tower, in the middle. You start the hard climb up. It is very steep. The other team is catching up now. You climb faster. You slip! You fall! You die! Not really, your partner caught your hand and saved you. You hurry back up. You reach the top. The other team does as well. You both reach for the buzzer but it falls down to earth. Luckily your partner is lower than you, and caught the buzzer. You climb down a little and together you both press the buzzer with all your might.')
Winner = Room('You Win!',                       None, None, None, None, None, None, None,                                      'You all climb down. When you reach the bottom, there are many people cheering and vodka bottles are spraying everywhere. You shake the other team’s hands, they have been a good opponent. You have done it! You have won the 1 million dollars! Good job, you have earned it! :)')

node = Intro  #Beggining Room

while True:
    print "ROOM: " + node.name  #prints name of room
    print
    print "DESCRIPTION: " + node.description   #prints description of room
    print
    command = raw_input(">").strip().lower() #gets your command
    if command in ['q', 'quit', 'exit']:     #you can exit mid-game
        sys.exit(0)
    if command in ['north', 'south', 'east', 'west', 'down', 'up', 'use']:  #if possible movement path
        try:
            node.move(command)   #then move
        except:
            print "That command is invalid. Sorry, maybe you should try going another way."   #if not then say so
    if command in 'use':  #if command starts a function
        try:
            function = node.use
            function()    #then it will run that function
        except:
            pass
    if dead:          #if you died in Russian Roulette, then you die and the game ends. 
        sys.exit(0)
    if node.name == 'You Win!' and unlock_room == False:  #if you get to the winning room but you did not finish the challenge then you loose. You had to do the challenge
        print "Sorry, you did not win a game of hangman, which was one of your challenges. You had to do that to win. Because of that, you have lost. The million dollars goes to the other team, sorry."
        sys.exit(0)
    else:
        Win = True
        pass   #otherwise you win the game. 
        
    if node.name == 'You Win!' and Win == True:  #if you get to the winning room and you finished the challenge then you win. 
        print "ROOM: " + node.name  #prints name of room
        print
        print "DESCRIPTION: " + node.description   #prints description of room
        raise SystemExit