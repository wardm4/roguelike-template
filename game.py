import pygcurse, pygame, sys, time, random
from pygame.locals import *

#Main Window size and name
win = pygcurse.PygcurseWindow(60, 30)
pygame.display.set_caption('Pygcurse Test')
win.autowindowupdate = False
win.autoupdate = False

#A rudimentary class that stores the character's position and health

class Character(object):
    def __init__(self, posx, posy):
        self.health = 5
        self.posx = posx
        self.posy = posy

    def attack(self, opponent):
        if random.random() > 0.5:
            self.health -= 1
        else:
            opponent.health -= 1


#Some simple auxilary functions

def testposition(x,y):
    return x >= 10 and x < 60 and y >= 5 and y < 30

def randx():
    return random.randint(11,59)

def randy(): 
    return random.randint(6, 29)


#Start the main pygame function

def main():

    #Initialize some values

    moveUp = moveDown = moveLeft = moveRight = False
    hero = Character(randx(), randy())
    enemy = Character(randx(), randy())

    #Start the game loop

    t = 0
    while True:

        pygame.event.set_allowed(None)
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])
        e = pygame.event.wait()
        pressed = e.key

    
        #Get input with standard vi keybinding or arrow keys

        if pressed == 8:
            newGame = True
        elif pressed == 27:
            pygame.quit()
            sys.exit()
        elif pressed == 273 or pressed == 107:
            moveUp = True
        elif pressed == 274 or pressed == 106:
            moveDown = True
        elif pressed == 276 or pressed == 104:
            moveLeft = True
        elif pressed == 275 or pressed == 108:
            moveRight = True
        elif pressed == 117:
            moveRight = True
            moveUp = True
        elif pressed == 121:
            moveLeft = True
            moveUp = True
        elif pressed == 110:
            moveRight = True
            moveDown = True
        elif pressed == 98:
            moveLeft = True
            moveDown = True
              
            

        # move the player (if allowed)
        
        if moveUp and (hero.posx, hero.posy) != (enemy.posx,enemy.posy+1) and testposition(hero.posx, hero.posy-1):
            hero.posy -= 1
        if moveDown and (hero.posx, hero.posy) != (enemy.posx,enemy.posy-1) and testposition(hero.posx, hero.posy+1):
            hero.posy += 1
        if moveLeft and (hero.posx, hero.posy) != (enemy.posx+1,enemy.posy) and testposition(hero.posx-1, hero.posy):
            hero.posx -= 1
        if moveRight and (hero.posx, hero.posy) != (enemy.posx-1,enemy.posy) and testposition(hero.posx+1, hero.posy):
            hero.posx += 1

        #A very basic 50/50 attack system

        if moveUp and (hero.posx, hero.posy) == (enemy.posx,enemy.posy+1):
            hero.attack(enemy)
        elif moveDown and (hero.posx, hero.posy) == (enemy.posx,enemy.posy-1):
            hero.attack(enemy)
        elif moveLeft and (hero.posx, hero.posy) == (enemy.posx+1,enemy.posy):
            hero.attack(enemy)
        elif moveRight and (hero.posx, hero.posy) == (enemy.posx-1,enemy.posy):
            hero.attack(enemy)

        moveUp = moveDown = moveLeft = moveRight = False
        t += 1


        # Display the "dungeon" and character info, playing with these colors
        # will certainly result in something more pleasing to the eye.

        win.fill('.', region = (10, 5, 50, 25), fgcolor='silver', bgcolor='olive')
        win.putchar('@', hero.posx, hero.posy)
        win.putchar('v', enemy.posx, enemy.posy)
        win.write('Your health: ' + str(hero.health), 10, 0, fgcolor='white')
        win.write('Virus health: ' + str(enemy.health), 10, 1, fgcolor='white')
        win.write('Turn: ' + str(t), 0, 5, fgcolor='white')
        win.write('Items:', 0, 6, fgcolor='white')
        win.update()
        pygame.display.update()
        
        #Test for the end of the game and break out if over

        if hero.health == 0:
            break

        if enemy.health == 0:
            break

    #Display whether you won or lost    
        
    if hero.health == 0:
        win.write('You lose.', 10, 2, fgcolor='white')
        win.update()
        pygame.display.update()
        time.sleep(5)
        pygcurse.waitforkeypress()

    if enemy.health == 0:
        win.write('You win!', 10, 2, fgcolor='white')
        win.update()
        pygame.display.update()
        time.sleep(5)
        pygcurse.waitforkeypress()
  
        


if __name__ == '__main__':
    main()