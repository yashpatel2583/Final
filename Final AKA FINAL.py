#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
# -*- coding: utf-8 -*-
#Choose: Name, Gender, Age, Money,
#This was not here before
import sys
import collections
import itertools
import random
compass = ('n','e','s','w','u','d','r','l','north','east','west','right','left','south','up','down','N','E','S','W','U','D','R','L','North','East','West','Right','Left','South','Up','Down')

dialogue_node = 'Intro'

def display_options(node):
    print '\nYour Options'
    for i,p in enumerate(node['Compass']):
        print '\t%d: "%s"' % (i, p[1])

def player_says(destination, text):
    global dialogue_node
    print 'You say: "%s"' % text
    dialogue_node = destination 


Dialogue = {
    'Intro' : {
        'Description' : 'This is a Adventure Text based game, Dont forget to go to the direction where sun rises, Good Luck Have Fun.... :)  ',
        }
        
}

while True:
    node = Dialogue[dialogue_node]
    #Talks
    print  '%s' % node['Description']
    break
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
account_balance = 100000
def deposit(money): #adds money to balance 
    global account_balance
    account_balance += money
    print "Your new account balance is:", account_balance
    
def withdraw(money): #takes money from balance
    global account_balance
    account_balance -= money
    print "Your new account balance is:", account_balance

    #deposit(4.00)
    #withdraw(2.00)
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     

Stats = {'ability' : '',                      
        'ClassRace' : '',
        'AbilityScore' : {
            'Strength': '',
            'Dexterity': '',
            'Experience': '',
            'Inteligence': '',
            },
        'GP' : '',
        'clothes' : '' ,
        'CName' : '',
        'gender' : '', 
        'age' : '', 
        'appearance' : '',
        'lang' : ''
}

def Name():                                  
    name = raw_input("What's your name? : ")
    Stats['Name'] = name                      


def rollability():                           
    list_of_numbers = [random.randint(1,6) for i in range(4)]
    added_sum = sum(list_of_numbers) - min(list_of_numbers) 
    Stats['ability'] = added_sum             


def class_race():
    classes = "barbarian", "Spear Goblin", "Archer", "Valkyrie", "Knight", "Giant", "Musketeer", "Prince", "Minions", "P.E.K.K.A.", "Golem"   
    race = "human", "Robot", "Hog_Rider", "halflings", "Musketeers", "Goblins"   
    cla = random.choice(classes)  
    rac = random.choice(race)      
    print "You are a", rac, cla   
    Stats['ClassRace'] = rac, cla  

                
def abilityscore():               
    print "You have 6 catagories for your Abilities. They are Strength, Dexterity, Experience and Inteligence."
        
    total = Stats['ability']       
    print "Your Strength is", total  
    Stats['AbilityScore']['Strength'] = total  
    rollability()       
    
    total = Stats['ability']      
    print "Your Dexterity is", total  
    Stats['AbilityScore']['Dexterity'] = total  
    rollability()       
    
    total = Stats['ability']      
    print "Your Experience is", total  
    Stats['AbilityScore']['Experience'] = total  
    rollability()       
    
    total = Stats['ability']      
    print "Your Inteligence is", total  
    Stats['AbilityScore']['Inteligence'] = total  
    rollability()       
    


def adjust():            
    print "You are a", Stats['ClassRace'][0], Stats['ClassRace'][1]  
    print "That means..."
    
    if Stats['ClassRace'][0] == "human":            
        print "Your ability stays the same."
        
    if Stats['ClassRace'][0] == "Robot":   
        Stats['AbilityScore']['Experience'] += 2
        print "Your Experience is now", Stats['AbilityScore']['Experience']  
        
    if Stats['ClassRace'][0] == "elf":    
        Stats['AbilityScore']['Dexterity'] += 2
        print "Your Dexterity is now", Stats['AbilityScore']['Dexterity']  
        Stats['AbilityScore']['Experience'] -= 2
        print "Your Experience is now", Stats['AbilityScore']['Experience']  
        
    if Stats['ClassRace'][0] == "Horse_Man":  
        Stats['AbilityScore']['Experience'] += 2
        print "Your Experience is now", Stats['AbilityScore']['Experience']  
        Stats['AbilityScore']['Strength'] -= 2
        print "Your Strength is now", Stats['AbilityScore']['Strength']  
        
    if Stats['ClassRace'][0] == "Musketeers":            
        print "Your ability stays the same."
        
    if Stats['ClassRace'][0] == "Goblins":   
        Stats['AbilityScore']['Strength'] += 2
        print "Your Strength is now", Stats['AbilityScore']['Strength']  
        Stats['AbilityScore']['Inteligence'] -= 2         
        if Stats['AbilityScore']['Inteligence'] <= 3:     
            Stats['AbilityScore']['Inteligence'] = 3      
            print "Your Inteligence is now", Stats['AbilityScore']['Inteligence']   
        else:
            print "Your Inteligence is now", Stats['AbilityScore']['Inteligence']   
        
        
    if Stats['ClassRace'][0] == "halflings":   
        Stats['AbilityScore']['Dexterity'] += 2
        print "Your Dexterity is now", Stats['AbilityScore']['Dexterity']
        Stats['AbilityScore']['Strength'] -= 2 
        print "Your Strength is now", Stats['AbilityScore']['Strength']
    
    if Stats['ClassRace'][1] == "Archer":      
        print "You can speak Abyssal, Celestial, and Infernal."   
        Stats['lang'] = "Abyssal, Celestial, and Infernal"
    if Stats['ClassRace'][1] == "Valkyrie":      
        print "You can speak Sylvan"           
        Stats['lang'] = "Sylvan"
    if Stats['ClassRace'][1] == "Golem":      
        print "You can speak Draconic"       
        Stats['lang'] = "Draconic"
    else:
        print "You can't speak special languges."    
        Stats['lang'] = "no special languages"
              
              
def Equipment():
    if Stats['ClassRace'][1] == "barbarian":
        one = random.choice(range(5))
        two = random.choice(range(5))
        three = random.choice(range(5))
        four = random.choice(range(5))  
        total = one + two + three + four     
        Stats['GP'] = total
        if Stats['GP'] == 0:
            print 'You broke'
        else: 
            print "You have %d gold pieces" % Stats["GP"]                      
        
    if Stats['ClassRace'][1] == "Spear Goblin":
        one = random.choice(range(5))
        two = random.choice(range(5))
        three = random.choice(range(5))
        four = random.choice(range(5))  
        total = one + two + three + four
        Stats['GP'] = total
        if Stats['GP'] == 0:
            print 'You broke'
        else: 
            print "You have %d gold pieces" % Stats["GP"]                      
        
    if Stats['ClassRace'][1] == "Archer":
        one = random.choice(range(5))
        two = random.choice(range(5))
        three = random.choice(range(5))
        four = random.choice(range(5))
        five = random.choice(range(5))  
        total = one + two + three + four + five
        Stats['GP'] = total
        if Stats['GP'] == 0:
            print 'You broke'
        else: 
            print "You have %d gold pieces" % Stats["GP"]                          
        
    if Stats['ClassRace'][1] == "Valkyrie":
        one = random.choice(range(5))
        two = random.choice(range(5))
        total = one + two
        Stats['GP'] = total
        if Stats['GP'] == 0:
            print 'You broke'
        else: 
            print "You have %d gold pieces" % Stats["GP"]                           
        
    if Stats['ClassRace'][1] == "Knight":
        one = random.choice(range(5))
        two = random.choice(range(5))
        three = random.choice(range(5))
        four = random.choice(range(5))
        five = random.choice(range(5))  
        six = random.choice(range(5))
        total = one + two + three + four + five + six
        Stats['GP'] = total
        if Stats['GP'] == 0:
            print 'You broke'
        else: 
            print "You have %d gold pieces" % Stats["GP"]                               
        
    if Stats['ClassRace'][1] == "Giant":
        one = random.choice(range(5))
        two = random.choice(range(5))
        three = random.choice(range(5))
        four = random.choice(range(5))
        five = random.choice(range(5))  
        total = one + two + three + four + five
        Stats['GP'] = total, "and 5 silver pieces"
        if Stats['GP'] == 0:
            print 'You broke'
        else: 
            print "You have %d gold pieces" % Stats["GP"]      
        
    if Stats['ClassRace'][1] == "Musketeer":
        one = random.choice(range(5))
        two = random.choice(range(5))
        three = random.choice(range(5))
        four = random.choice(range(5))
        five = random.choice(range(5))  
        six = random.choice(range(5))
        total = one + two + three + four + five + six
        Stats['GP'] = total
        if Stats['GP'] == 0:
            print 'You broke'
        else: 
            print "You have %d gold pieces" % Stats["GP"]                        
        
    if Stats['ClassRace'][1] == "Prince":
        one = random.choice(range(5))
        two = random.choice(range(5))
        three = random.choice(range(5))
        four = random.choice(range(5))
        five = random.choice(range(5))  
        six = random.choice(range(5))
        total = one + two + three + four + five + six
        Stats['GP'] = total
        if Stats['GP'] == 0:
            print 'You broke'
        else: 
            print "You have %d gold pieces" % Stats["GP"]                          
        
    if Stats['ClassRace'][1] == "Minions":
        one = random.choice(range(5))
        two = random.choice(range(5))
        three = random.choice(range(5))
        four = random.choice(range(5))
        five = random.choice(range(5))  
        total = one + two + three + four + five
        Stats['GP'] = total
        if Stats['GP'] == 0:
            print 'You broke'
        else: 
            print "You have %d gold pieces" % Stats["GP"]                      
        
    if Stats['ClassRace'][1] == "sorcerer":
        one = random.choice(range(5))
        two = random.choice(range(5))
        three = random.choice(range(5))
        total = one + two + three
        Stats['GP'] = total
        if Stats['GP'] == 0:
            print 'You broke'
        else: 
            print "You have %d gold pieces" % Stats["GP"]                        
        
    if Stats['ClassRace'][1] == "Golem":
        one = random.choice(range(5))
        two = random.choice(range(5))
        three = random.choice(range(5))
        total = 0#one + two + three
        Stats['GP'] = total                    
        if Stats['GP'] == 0:
            print 'You broke'
        else: 
            print "You have %d gold pieces" % Stats["GP"]                  


def clothes():
    types = "Janitor's outfit", "Stealth's outfit", "Exterminator's outfit", "Hunting outfit", "Tuxedo's outfit", "Protector's outfit", "Wastelander's outfit"   
    yours = random.choice(types)    
    Stats['clothes'] = yours        
    print "You are wearing a", Stats['clothes']    
    
    
def playerName():                                  
    Cname = raw_input("What do you want your character's name to be? : ")
    Stats['CName'] = Cname                      
    print "Ok"
 
   
def gender():
    genders = "male", "female",
    you = random.choice(genders)    
    Stats['gender'] = you            
    print "You are", Stats['gender']  
    

def age():        
    age = random.randint(1, 99)  
    Stats['age'] = age   
    print "You are", age, "years old."   
    
    
def appearance():
    types = "pretty", "handsome",    
    you = random.choice(types)    
    Stats['appearance'] = you      
    print "You are", you          


def ending():    
    print 
    print
    print Stats['Name'], "your characters name is", Stats['CName'], "who is a", Stats['appearance'], Stats['gender'], Stats['ClassRace'][0], Stats['ClassRace'][1]
    print "You are", Stats['age'], "years old"
    print "Your strength is", Stats['AbilityScore']['Strength']
    print "Your Dexterity is", Stats['AbilityScore']['Dexterity']
    print "Your Experiance is", Stats['AbilityScore']['Experience']
    print "Your inteligence is", Stats['AbilityScore']['Inteligence']
    print "You speak", Stats['lang']
    print "You have", Stats['GP'], "gold pieces"
    print "You wear", Stats['clothes']






print "Lets play the Game!"       
print                                         
Name()                                          
print                                          
rollability()                                 
print                                         
class_race()                                   
print                                         
abilityscore()                                 
print                                          
adjust()                                        
print                                      
Equipment()                                   
print                                       
clothes()                                 
print                                          
playerName()                             
print                                          
gender()                                 
print                                       
age()                                      
print                                       
appearance()                                 
print                                   
ending()                                     
print                                       
print                                        
print "That is your player."   
print
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
player_location = 'Office'  #The room you're in at the start of the game

#gives possible options
def Give_options(node):
    print '\nYour Options:'
    for i,p in enumerate(node['PATHS']):
        print '\t%d: "%s"' % (i, p[2])

#moves between rooms       
def change_room(room):
    global player_location
    player_location = room

#end of game if you die
def die(death_reason):
    print "\n\n" + death_reason + "\n You Lose."
    sys.exit()

#options for dialogue   
def display_options_diologue(node):
    print '\nYour options:'
    for i,p in enumerate(node['PATHS']):
        print '\t%d: "%s"' % (i, p[1])
        
#starts the conversation      
def start_conversation(character):
    dictionary = globals()[character]
    node = dictionary[character]
    dialogue_node = character
    while True:
        node = dictionary[dialogue_node]
        
        #shows who says what
        print '%s says: %s' % (character, node['DESCRIPTION'])
        
        #gives options
        display_options_diologue(node)
        
        #prompt
        next_command = raw_input('>')
        
        #Quit when I want        
        if next_command in ['q', 'quit']:
            sys.exit(0)
            
        elif 'PATHS' in node:    
            #Try to move    
            try:
                path = node['PATHS'][int(next_command)]
                dialogue_node = path[0]
                
            except:
                print 'Invalid number. Why don\'t you try a valid number.'
        else:
            break


World_map = { #this is the map of this "world"
            'Office' : {
                'DESCRIPTION' : 'Hello! Your mission in this Motel is to find Your_Room, and find as many secreates as you can before Exiting Motel, but first "Talk to Manager" ',
                'PATHS' : [
                    (change_room, 'Window', 'Go north'),
                    (change_room, 'open letter', 'Open the letter'),
                    (start_conversation, 'Manager', 'Talk to Manager')
                          ]
                         },
            'open letter' : {
                'DESCRIPTION' : 'For Secret Missions, dont forget to type use for hidden Games in the room you think there might be Game "Be Careful"',
                'PATHS' : [
                    (change_room, 'Window', 'Go north'),
                          ]
                         },
            'Window' : {
                'DESCRIPTION' : 'There is Beautiful lightning water show going on and there are some Gorgeous Casinos',
                'PATHS' : [
                    (change_room, 'Water_Lake', 'Jump'),
                    (change_room, 'Soda_Machine', 'Go south')
                          ]
                                },
            'Water_Lake' : {
                'DESCRIPTION' : 'You jump out of the Office window. You fall in Water and you are injured find Your_Room as Soon as you can to get Medical Aid',
                'PATHS' : [
                    (change_room, 'Exit', 'Exit_Office')
                            ]
                                },
                                
            'Exit' : {
                'DESCRIPTION' : 'You have Sucessfully Exit the Office please Continue to Your_Room',
                },
                
            'Drawer' : {
                'DESCRIPTION' : 'You try very hard to open the drawer but Unfortunately the Drawer is Locked',
                'PATHS' : [
                    (change_room, 'Soda_Machine', 'Go down'),
                    (change_room, 'Rug', 'Move the Rug')
                          ]
                                },
            'Soda_Machine' : {
                'DESCRIPTION' : 'There is A Soda_Machine you want to drink a Soda and you are Thursty, Would you buy a Soda',
                'PATHS' : [
                    (change_room, 'yes', 'Yes'),
                    (change_room, 'no', 'No')
                          ]
                                },
            'yes' : {
                'DESCRIPTION' : 'You drink the drink Coke and your Thurst Level is now 100.',
                'PATHS' : [
                    (change_room, 'Exit', 'Go west')
                    ]
                                },
            'no' : {
                'DESCRIPTION' : 'You refuse to buy soda, your Thurst Level is now 75',
                'PATHS' : [
                    (change_room, 'Exit', 'Go west')
                    ]
                                },

            'Rug' : {
                'DESCRIPTION' : 'With a great effort, the rug is moved to the side but unfortunately is only DUST LOL',
                'PATHS' : [
                    (change_room, 'Door_1', 'Go north'),
                    (change_room, 'Risk_level3', 'Go west'),
                          ]
                                },
                                
                    
            
    
}

Manager = {   #this is the dialogue with Manager
            'Manager' : {
                'DESCRIPTION' : 'Welcome to Travel inn and Suits .Would you like to buy room?',
                'PATHS' : [
                    ('Yes', 'Yes'),
                    ('No', 'No'),
                    ]
                },
                'Yes' : {
                'DESCRIPTION' : 'There is only Non - Smoking room left for you and is the last room we have, Would you still like to buy the Room?.',
                'PATHS' : [
                    ('Non - Smoking', 'Yes, I would like to buy the Room',),
                    ('Bye', 'No then Press "q" to quit'),
                    ]
                },
            'Non - Smoking' : {
                'DESCRIPTION' : 'Thanks for your Business. To gain Intelligence Find Your_Room',
                'PATHS' : [
                    ('Bye', 'Thanks')
                    ]
                },
            'No' : {
                'DESCRIPTION' : 'Please press "q" to quit',
                'PATHS' : [
                    ('Yes', 'Have you changed your mind and still like to buy Room?')
                    ]
                },
            
            'Bye' : {
                'DESCRIPTION' : ' You can Start towards your Destination',
                },

}
	
while True:
    room = World_map[player_location]
        
    #tell us where we are
    print player_location
    print room['DESCRIPTION']
    
    #if the room has no paths it stops the game     
    if not room.has_key('PATHS'):
     break
    
    #gives options
    Give_options(room)
    
    #prompt
    command = raw_input('>')
    
    #Quit when I want        
    if command in ['q', 'quit']:
     sys.exit(0)
    
    #Try to move    
    try:
        path = room['PATHS'][int(command)]
        function = path[0]
        args = path[1]
        function(args)
        
    except:
        print 'Invalid number. Try a valid number.'

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
# -*- coding: utf-8 -*-


node = None  #variable that will later tell you where you start the game
unlock_room  = False  #variable that will be used to tell if you win the game or not. It it is true later, then you win, if it is still false, you loose. 
dead = False #possible death variable in Russian Roulette. 
Win = False
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
def Tic():
    def print_board(board):
    
   	    print "The board look like this: \n"
    
   	    for i in range(3):
  	        	print " ",
  	        	for j in range(3):
	         		if board[i*3+j] == 1:
	        			print 'X',
	         		elif board[i*3+j] == 0:
	        			print 'O',	
	         		elif board[i*3+j] != -1:
	        			print board[i*3+j]-1,
	         		else:
	        			print ' ',
	     		
	         		if j != 2:
	        			print " | ",
	          	print
	  	
	          	if i != 2:
	         		print "-----------------"
	          	else: 
	         		print 
			
    def print_instruction():
           	print "Please use the following cell numbers to make your move"
           	print_board([2,3,4,5,6,7,8,9,10])


    def get_input(turn):

           	valid = False
           	while not valid:
          		try:
         			user = raw_input("Where would you like to place " + turn + " (1-9)? ")
         			user = int(user)
         			if user >= 1 and user <= 9:
         			        return user-1
         			else:
        				print "That is not a valid move! Please try again.\n"
        				print_instruction()
          		except Exception as e:
         			print user + " is not a valid move! Please try again.\n"
      		
    def check_win(board):
           	win_cond = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
           	for each in win_cond:
          		try:
         			if board[each[0]-1] == board[each[1]-1] and board[each[1]-1] == board[each[2]-1]:
        				return board[each[0]-1]
          		except:
         			pass
           	return -1
        

    def quit_game(board,msg):
           	print_board(board)
           	print msg
                sys.exit(0)



    def main():
   	
	# setup game
	# alternate turns
	# check if win or end
	# quit and show the board
	
           	print_instruction()
    
           	board = []
           	for i in range(9):
		  board.append(-1)

           	win = False
           	move = 0
           	while not win:

		# print board
          		print_board(board)
          		print "Turn number " + str(move+1)
              		if move % 2 == 0:
         			turn = 'X'
          		else:
         			turn = 'O'

		# get user input
          		user = get_input(turn)
          		while board[user] != -1:
         			print "Invalid move! Cell already taken. Please try again.\n"
         			user = get_input(turn)
          		board[user] = 1 if turn == 'X' else 0
    
		# advance move and check for end game
          		move += 1
          		if move > 4:
         			winner = check_win(board)
         			if winner != -1:
            				out = "The winner is " 
        				out += "X" if winner == 1 else "O" 
        				out += " :)"
        				quit_game(board,out)
         			elif move == 9:
        				quit_game(board,"No winner :(")

    if __name__ == "__main__":
           	main()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
def bank():

    account_balance = 1
    def deposit(money): #adds money to balance 
        global account_balance
        account_balance += money
        print "Your new account balance is:", account_balance
    
    def withdraw(money): #takes money from balance
        global account_balance
        account_balance -= money
        print "Your new account balance is:", account_balance


#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#Hangman Minigame
def hangman():
    print "You will gain Intelligence, Strength and XP from playing this game. "
    print
    
    allwords = "mouse", "laptop", "espanol", "fire", "mr", "ms", "mrs", "test", "taking", "take", "tips", "congruent", "protractor", "step", "steps", "signs", "sign", "exit", "enter", "not", "who", "you", "are", "that", "gaming", "question", "questions", "holds", "you", "back", "think", "thought", "games", "game", "fabric", "cloth", "screw", "nail", "hammer", "squirt", "picture", "frame", "pictureframe", "for", "it", "is", "tape", "box", "phone", "cellphone", "user", "username", "password", "pass", "ruler", "measure", "comfortable", "the", "a", "alright", "day", "days", "bench", "brick", "bricks", "earaser", "pad", "panel", "tempeture", "blackborad", "chalk", "cube", "statue", "january", "febuary", "march", "april", "may", "june", "july", "august", "october", "november", "december", "month", "months", "ice", "door", "drawing", "liberty", "well", "good", "qiuz", "objective", "geometry", "math", "english", "spanish", "video", "food", "case", "water", "soda", "pyramid", "overhead", "projector", "umbrella", "textbook", "text", "bookcase", "tacos", "burritos", "wiebe", "kyle", "volume", "control", "error", "whipe", "pen", "trash", "gear", "clock", "stool", "chair", "desk", "grease", "bread", "motor", "marker", "monitor", "wire", "input", "fit", "cane", "stack", "weed", "drugs", "pinter", "back", "whiteboard", "wood", "metal", "code", "Bible", "binder", "paper", "hilighter", "pencil", "bucket", "round", "circular", "hangman", "bottle", "nag", "expo", "green", "all", "word", "cabinet", "banner", "turtle", "mouse", "jellyfish", "peanuts", "whale", "tiger", "panther", "couger", "words", "flag", "chair", "triangle", "circle", "square", "trapaziod", "hexagon", "blue", "orange", "purple", "brown", "black", "white", "red", "moroon", "gold", "silver", "bronze", "medallion", "medal", "book", "movie", "trip", "car", "bike", "trike", "tricycle", "moped", "I", "ice", "idea", "ideal", "identical", "identification", "identify",  "bye", "hi", "if", "ignore", "ill", "illegal", "illness", "illustrate", "image", "imaginary", "imagination", "imaginative", "imagine", "imitate", "immediate", "immigrant", "immoral", "impact", "impatience", "impatient", "import", "stuff", "all", "cool", "nice", "zero", "zone", "zoo", "dog", "cat", "chat", "illuminati", "computer", "hello", "yard", "yawn", "year", "yearly", "yell", "yellow", "yes", "yesterday", "yet", "you", "young", "your", "yours", "yourself", "loooooser", "winner", "alligator", "llama", "comotellamas", "supercalifragilisticexpialidocious", "table", "tactful", "tactless", "tail", "take", "takeoff", "talent", "talk", "tall", "tank", "tap", "tape", "target", "task", "taste", "tax", "taxi", "tea", "teach", "teacher", "team", "teammate", "tear", "technical", "technique" #this is the list of possible words
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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#Russian Roulette Minigame                                
def RR():
    global dead                                              
    fullgun = "barrel 1", "barrel 2", "barrel 3", "barrel 4", "barrel 5", "barrel 6"
    chosen = random.choice(fullgun)    #randon barrel  -  what you got
    bulletIn = random.choice(fullgun)  #random barrel  -  where bullet is
    message = "You were not suppose to type 'use'"
    
    print message  #prints above message which introduces the situation
    print
    print "Prepare yourself."
    print
    print "You Killed Yourself "  #suspence
    if bulletIn == chosen:
        print "You were Killed"    #if they are the same you die, and the game ends.
        dead = True   #if you die, then dead will be true and you will exit the game. 
        raise SystemExit
    else:
        print ""  #if not, you survive and continue on your way. 

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
def Poker():                      
    

    
    SUIT_LIST = ("Hearts", "Spades", "Diamonds", "Clubs")
    NUMERAL_LIST = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace")

    class card:
        def __init__(self, numeral, suit):
            self.numeral = numeral
            self.suit = suit
            self.card = self.numeral, self.suit
        def __repr__(self):
            return self.numeral + "-" + self.suit

    class poker_hand():
        def __init__(self, card_list):
            self.card_list = card_list
        def __repr__(self):
            short_desc = "Nothing."
            numeral_dict = collections.defaultdict(int)
            suit_dict = collections.defaultdict(int)
            for my_card in self.card_list:
                numeral_dict[my_card.numeral] += 1
                suit_dict[my_card.suit] += 1
            # Pair
            if len(numeral_dict) == 4:
                short_desc = "One pair."
            # Two pair or 3-of-a-kind
            elif len(numeral_dict) == 3:
                if 3 in numeral_dict.values():
                    short_desc ="Three-of-a-kind."
                else:
                    short_desc ="Two pair."
            # Full Your_Room or 4-of-a-kind
            elif len(numeral_dict) == 2:
                if 2 in numeral_dict.values():
                    short_desc ="Full Your_Room."
                else:
                    short_desc ="Four-of-a-kind."
            else:
                # Flushes and straights
                straight, flush = False, False
                if len(suit_dict) == 1:
                    flush = True
                min_numeral = min([NUMERAL_LIST.index(x) for x in numeral_dict.keys()])
                max_numeral = max([NUMERAL_LIST.index(x) for x in numeral_dict.keys()])
                if int(max_numeral) - int(min_numeral) == 4:
                    straight = True
                # Ace can be low
                low_straight = set(("Ace", "2", "3", "4", "5"))
                if not set(numeral_dict.keys()).difference(low_straight):
                    straight = True
                if straight and not flush:
                    short_desc ="Straight."
                elif flush and not straight:
                    short_desc ="Flush."
                elif flush and  straight:
                    short_desc ="Straight flush."
            enumeration = "/".join([str(x) for x in self.card_list])
            return "{enumeration} ({short_desc})".format(**locals())
    
    class deck(set):
        def __init__(self):
            for numeral, suit in itertools.product(NUMERAL_LIST, SUIT_LIST):
                self.add(card(numeral, suit))
        def get_card(self):
            a_card = random.sample(self, 1)[0]
            self.remove(a_card)
            return a_card
        def get_hand(self, number_of_cards=5):
            if number_of_cards == 5:
                return poker_hand([self.get_card() for x in range(number_of_cards)])
            else:
                raise NotImplementedError
    
    for i in range(7):
        print(deck().get_hand())
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------     
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ 

class Room:
    #Constructor
    def __init__(self, name, north, south, east, west, down, up, use, description):
        self.name = name
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.down = down
        self.up = up
        self.use = use
    #Movement Method
    def move(self, direction):
        global node
        node = globals()[getattr(self, direction)]

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------               
#ROOMS Motel
             #Room Name                         #N    #S    #E    #W    #D    #U    #Use                                       #Description
Office = Room('Office',                    None, None, None, None, None, None, 'Dining_Room',                               'Hello! Your mission in this Motel is to find Your_Room, When you find the Your_Room, Exit the Motel and Continue to Explore some places, Good Luck Have Fun.   **** Type "use" to start the game ****' )
Dining_Room = Room('Dining_Room',          None, 'Parking_lot', 'Hallway', None, None, None, None,                          'You are in the Dining Room, there are lots of people waiting in line to eat delicious food, there is Hallway to your "east"')
Hallway = Room('Hallway',                  None, 'Parking_lot', 'Kitchen', 'Dining_Room', 'Kitchen', None, None,            'There are several doors. One to your west, and one to your south. Choose wisely..' )                                                                                                 
Kitchen = Room('Kitchen',                  None, None, 'Room_101', 'Hallway', 'Bank', 'Hallway', None,                      'You are in the kitchen. There Room_101 to your "east", people are looking at you tht who is this person and what are they doing here')
Cabinet = Room('Cabinet',                  None, 'Office', None, 'Kitchen', None, None, None,                               'The cabinet is locked it only opens with Code.')
Parking_lot = Room('Cabinet',             'Cabinet', None, 'Dead_End', None, None, None, None,                              'There is Lamborghini, Ferrari and some Best cars in the Parking_lot')
Dead_End = Room('Dead End',               'Room_101', 'Your_Room', None, 'Cabinet', None, None, None,                       'You are in a dead end. To the north is a Room_101. There is Construction going on to make some more Rooms and new Office')
Room_101 = Room('Room_101',                None, 'Dead_End', None, None, 'Your_Room', None, hangman,                        'You are in Room_101. Your_Room is to your "north"')
Your_Room = Room('Your_Room',             'Dead_End', None, 'Exit_Motel', None, None, None, hangman,                        'You find a secreat note saing Type ** use ** to play a secreat game to earn Xp and Intelligence .... finding your room your Xp is now 20 and your intelligence is now 22')
Exit_Motel = Room('Exit_Motel',           'School', None, None, 'Cabinet', None, None, RR,                                  'You have found Motels Exit You have gained 18 Exp and 20 Strength and 23 intelligence, You may Go and finish other Missions Good Luck...')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
School = Room('School',                    None, None, None, None, None, None, 'North_Admin',                           'Hello! Your mission in this School is make the author of this game to loose in Tic Tac Tao and play Hangman **** Type "use" to Continue the game **** or press "q" to quit' )
North_Admin = Room('North_Admin',                   None, None, 'School_Hallway', None, None, None, Tic,                          'You are in the North_Admin of the School, where there is Nurse, Vice-Principle and some other Staff this Room is also called "Attendence Office" **** Type "use" to play Tic-Tac-Tao game ****   To your "east" there is Hallway' )
School_Hallway = Room('School_Hallway',                             None, None, 'Cafeteria', 'North_Admin', 'Cafeteria', None, Poker,          'This is School_Hallway there might be secreat game here you know what to type to your "down" there is Cafetaria.' )                                                                                                 
Cafeteria = Room('Cafeteria',                           None, None, 'W_Building', 'School_Hallway', None, 'School_Hallway', None,           'You are in the Cafeteria. To your "east" there is W_Bj]uilding')
Science_Building = Room('Science_Building',                       None, 'Office', None, 'Cafeteria', None, None, 'Play_Ground',                 'You are just ouside of the North_Admin complex with your partner. You are on a sidewalk next to a street. You see a booth with the sign that says ’Info Center’. It has a map on it. It might help. There are also stores on the other side of the street. Such as ‘Russian Walmart’ and Russian ’El Polo Loco’. But you have no time to shop. You must go on.')
Play_Ground = Room('Info Center',               None, 'Science_Building', None, None, None, None, 'Science_Building',                         'You walk to the map on the Info Center. The map shows you that you are on the street ’Blackstone’. It goes north to south. The North_Admin complex was further north, and further south is an Science_Building where Blackstone and Ashlan meet. Ashlan goes west to east. But on the east is a dead end with abandoned buildings. On the west is the ’Church of the Savior on Blood’, the splendor of Russia. At the end of Blackstone, on the south is an alley.')
Science_Building = Room('Science_Building',             'Science_Building', None, 'Tech_Room', None, None, None, None,                                  'The Science_Building is locked it only opens with Code')
Tech_Room = Room('Tech_Room',                     'W_Building', 'South_Admin', None, 'Science_Building', None, None, None,                 'You are in a dead end. To the north is a W_Building. To the south is an South_Admin. West goes back to the Science_Building.')
W_Building = Room('W_Building',             None, 'Tech_Room', None, None, None, None, hangman,                                     'You are in an old W_Building. There are many old machines that once did something. Every step makes a creek. *BOOM!* A machine falls, revealing the other team behind it. They rush past you to the Science_Building. You must hurry to get ahead and win.')
South_Admin = Room('South_Admin',                 'Tech_Room', None, 'Exit_Motel', None, None, None, hangman,                               'You are in an old South_Admin. It was once an old nice South_Admin. Now it looks like it hasn’t been lived in you many years. You walk into the family room, but the other team rushes past you, out to the street. They must have seen that there was nothing to find here. You and your partner must hurry to get past them and win!')
Exit_School = Room('Exit_Motel',             'Bank', None, None, None, None, None, RR,                                  'You have found Motels Exit You have gained 18 Exp and 20 Strength and 22 intelligence, You may Go and finish other Missions Good Luck...')

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

node = Office  #Beggining Room

while True:
    print "ROOM: " + node.name  #prints name of room
    print
    print "DESCRIPTION: " + node.description   #prints description of room
    print
    print 'Direction(Type) :- "use" ,"north", "south", "east", "west", "down", "up"'
    print 'To Quit (Type) :- "q"'
    command = raw_input(">").strip().lower() #gets your command
    if command in ['q', 'quit', 'exit']:     #you can exit mid-game
        sys.exit(0)
    if command in ['use' ,'north', 'south', 'east', 'west', 'down', 'up',]:  #if possible movement path
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
        
        
        
        
        
        
        
        
