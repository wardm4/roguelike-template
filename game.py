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

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()


            #Get input with standard vi keybinding or arrow keys

            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    newGame = True
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_UP or event.key == K_k:
                    moveUp = True
                elif event.key == K_DOWN or event.key == K_j:
                    moveDown = True
                elif event.key == K_LEFT or event.key == K_h:
                    moveLeft = True
                elif event.key == K_RIGHT or event.key == K_l:
                    moveRight = True
                elif event.key == K_u:
                    moveRight = True
                    moveUp = True
                elif event.key == K_y:
                    moveLeft = True
                    moveUp = True
                elif event.key == K_n:
                    moveRight = True
                    moveDown = True
                elif event.key == K_b:
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


        # Display the "dungeon" and character info, playing with these colors
        # will certainly result in something more pleasing to the eye.

        win.fill('.', region = (10, 5, 50, 25), fgcolor='silver', bgcolor='olive')
        win.putchar('@', hero.posx, hero.posy)
        win.putchar('v', enemy.posx, enemy.posy)
        win.write('Your health: ' + str(hero.health), 10, 0, fgcolor='white')
        win.write('Virus health: ' + str(enemy.health), 10, 1, fgcolor='white')
        win.write('Items:', 0, 5, fgcolor='white')
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