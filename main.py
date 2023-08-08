# Complete your game here
import pygame
from random import randint

#Defines the main character of the game
class Robot:

    #set first position on the screen
    def __init__(self, initial_pos_x: int, initial_pos_y: int):
        self.x = initial_pos_x
        self.y = initial_pos_y

    #Moves the character by changing its x and y axes
    def move(self, x: int, y: int):
        self.x = x
        self.y = y

    #Returns coordinates to be processed
    def get_coordinates(self):
        return (self.x, self.y)

#Defines the coin properties
class Coin:

    #set first position on the screen
    def __init__(self, initial_pos_x: int, initial_pos_y: int):
        self.x = initial_pos_x
        self.y = initial_pos_y

    #Moves the character by changing its x and y axes
    def move(self, x: int, y: int):
        self.x = x
        self.y = y

    #Returns coordinates to be processed
    def get_coordinates(self):
        return (self.x, self.y)

#Defines the enemies on the screen     
class Monster:

    #Set first position on the screen and adds a speed factor to the characters
    def __init__(self, initial_pos_x: int, initial_pos_y: int):
        self.x = initial_pos_x
        self.y = initial_pos_y
        self.x_speed = 0

    #Moves the enemy only on x axis
    def move(self, x: int):
        self.x += x

    #resets position after reaching the end of the screen
    def reset_pos(self, initial_pos_x: int):
        self.x = initial_pos_x

    #sets the speed to each of the enemies
    def set_speed(self, speed: int):
        self.x_speed = speed

    #returns the speed to be used in the main game
    def get_speed(self):
        return self.x_speed

    #returns coordinates to be processed
    def get_coordinates(self):
        return (self.x, self.y)

#Defines the door character    
class Door:

    #Set first position
    def __init__(self, initial_pos_x: int, initial_pos_y: int):
        self.x = initial_pos_x
        self.y = initial_pos_y

    #Moves the door only on x axis
    def move(self, x: int):
        self.x = x

    #return coordinates to be processed
    def get_coordinates(self):
        return (self.x, self.y)

#Defines and handles all interaction between characters
class Game:

    #Loading all images
    robot_image = pygame.image.load('robot.png')
    coin_image = pygame.image.load('coin.png')
    monster_image = pygame.image.load('monster.png')
    door_image = pygame.image.load('door.png')

    #Defines the rect to use with collision method to detect if the player was captured by enemy
    rect_robot = robot_image.get_rect()

    #static variables to define if the main character moves or not
    to_right = False
    to_left = False
    to_up = False
    to_down = False

    #Initializes all characters and creates a list of enemies
    def __init__(self):
        self.monsters = []
        self.robot = Robot(0,0)
        self.coin = Coin(0,0)
        self.door = Door(0, 640 - self.door_image.get_height())
        
    #Populates the list of enemies
    def populate_monsters(self):
        number_of_monsters = 4
        height = self.monster_image.get_height()
        width = self.monster_image.get_width()
        adjust_Y = 100
        for i in range(number_of_monsters):
            monster = Monster(0 - width, adjust_Y)
            self.monsters.append(monster)
            adjust_Y += height + 50
    
    #Defines the coin position after loading the game and after increasing level
    def new_coin_position(self):
        rnd_x = randint(0, 640-self.coin_image.get_width()) #Random module used to define a random position
        self.coin.move(rnd_x, 0)
    
    #Defines the door position after loading the game and after increasing level
    def new_door_position(self):
        rnd_x = randint(0, 640-self.door_image.get_width()) #Random module used to define a random position
        self.door.move(rnd_x)

    #Defines a distinct speed to each enemy
    def set_monsters_speed(self):
        for monster in self.monsters:
            rnd_speed = randint(1, 15) #Random module used to define a random position
            monster.set_speed((1 + (rnd_speed/10)))
            
    #Main method - plays the game    
    def play(self):

        #Sets the title
        pygame.display.set_caption("Bring coins back home... and survive!")

        #Calls all methods to start the game
        self.populate_monsters()
        self.new_coin_position()
        self.new_door_position()
        self.set_monsters_speed()

        #Initializes the screen
        pygame.init()
        display = pygame.display.set_mode((640, 640))
        display.fill((80, 80, 80))

        #Clock used to defines fps
        clock = pygame.time.Clock()

        #Useful variables to be used in the game
        robot_width = self.robot_image.get_width()
        robot_height = self.robot_image.get_height()
        coin_width = self.coin_image.get_width()
        coin_height = self.coin_image.get_height()
        door_width = self.door_image.get_width()
        monster_width = self.monster_image.get_width()
        monster_height = self.monster_image.get_height()
        speed = 0
        x = 0
        y = 0
        hold_coin = False
        pause_screen = False
        level = 1

        #The loop reads keyboard keys pressed and defines the interaction between characters
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.to_left = True
                    if event.key == pygame.K_RIGHT:
                        self.to_right = True
                    if event.key == pygame.K_UP:
                        self.to_up = True
                    if event.key == pygame.K_DOWN:
                        self.to_down = True
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_r:
                        self.monsters.clear() #Resets the enemies list
                        self.play()           #Calls play method to restart

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.to_left = False
                    if event.key == pygame.K_RIGHT:
                        self.to_right = False
                    if event.key == pygame.K_UP:
                        self.to_up = False
                    if event.key == pygame.K_DOWN:
                        self.to_down = False

            #Populates the screen with enemies
            for monster in self.monsters:

                rect_monster = pygame.Rect(0, 0, monster_width, monster_height) #Defines a rect to each enemy to be used in the collision method
                if monster.get_coordinates()[0] >= 640:                         #Detects if the enemy reached the end of the screen and resets its position
                    monster.reset_pos(0 - monster_width)
                
                monster.move(monster.get_speed() + speed)                       #Adds movement to the enemy
                display.blit(self.monster_image, monster.get_coordinates())     #Draws the enemy on the screen

                self.rect_robot.x = self.robot.get_coordinates()[0]             #Adjust position of the "rects" to detect collision
                self.rect_robot.y = self.robot.get_coordinates()[1]
                rect_monster.x = monster.get_coordinates()[0]
                rect_monster.y = monster.get_coordinates()[1]

                if self.rect_robot.colliderect(rect_monster):                   #Verifies collision between the character and any of the enemies
                    pause_screen = True
            
            display.blit(self.robot_image, self.robot.get_coordinates())        #Draws the main character
            
            if not hold_coin:
                display.blit(self.coin_image, self.coin.get_coordinates())      #Verifies if the character is not holding the coin

            if hold_coin:                                                       #Checks if the player caught the coin, if yes, the coin follows the character moves
                self.coin.move(x + (robot_width/2) - (coin_width/2) , y + (650 - (robot_height/2) - coin_height/2))
                display.blit(self.coin_image, self.coin.get_coordinates())

        
            display.blit(self.door_image, self.door.get_coordinates())         

            game_font = pygame.font.SysFont("Verdana", 20)                      #Displays level on screen
            text = game_font.render(f"Level: {level}", True, (255, 0, 0))
            display.blit(text, (520, 25))

            #Freezes the screen in case of collision, adds info to the user to exit or restart the game and displays the level reached                                                                    
            if pause_screen:
                display.fill((255, 0, 0))
                text = game_font.render(f"You reached level {level}!", True, (255, 255, 255))
                option = game_font.render(f'Press "R" to restart', True, (255, 255, 255))
                display.blit(text, (220, 250))
                display.blit(option, (220, 300))
                option = game_font.render(f'Or "ESC" to exit', True, (255, 255, 255))
                display.blit(option, (220, 350))
                self.to_left = False
                self.to_right = False
                self.to_up = False
                self.to_down = False
            
            pygame.display.flip()

            #Moves the player if any of the parameters is true (defined by key pressed)
            if self.to_up:
                y -= 1 + speed
            if self.to_down:
                y += 1 + speed
            if self.to_right:
                x += 1 + speed
            if self.to_left:
                x -= 1 + speed
            
            #Updates the character position
            self.robot.move(x , y + 640 - robot_height)
            display.fill((80, 80, 80))

            #Conditions to check if the character has reached the screen borders and stop its movement
            if self.robot.get_coordinates()[0] <= 0:
                x = 0
            elif self.robot.get_coordinates()[0] >= 640 - robot_width:
                x = 640 - robot_width
            if self.robot.get_coordinates()[1] <= 0:
                y = -(640 - robot_height)
            elif self.robot.get_coordinates()[1] >= 640 - robot_height:
                y = 0
            
            #Checks the position of the main character related to the coin, if it is in its range, catches the coin and define "hold_coin" variable as true
            if  (self.robot.get_coordinates()[0] + robot_width) >= self.coin.get_coordinates()[0] and self.robot.get_coordinates()[0] <= self.coin.get_coordinates()[0] + coin_width and self.robot.get_coordinates()[1] <= coin_height:
                hold_coin = True

            #Checks the position of the coin related to the door, if it is in its range, collects the coin, increases the game speed
            #Increases the level, sets the "hold_coin" variable as false and reset enemies, coin and door positions
            if (self.coin.get_coordinates()[0] + coin_width) >= self.door.get_coordinates()[0] and self.coin.get_coordinates()[0] <= self.door.get_coordinates()[0] + door_width and self.coin.get_coordinates()[1] >= self.door.get_coordinates()[1]:
                speed += 0.2
                level += 1
                hold_coin = False
                self.set_monsters_speed()
                self.new_door_position()
                self.new_coin_position()
                          
            clock.tick(60)
        
rob_and_coins = Game()
rob_and_coins.play()