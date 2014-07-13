import pygcurse, pygame, sys, time, random
from pygame.locals import *

win = pygcurse.PygcurseWindow(60, 30)
pygame.display.set_caption('Pygcurse Test')

win.autowindowupdate = False
win.autoupdate = False

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

def main():
    moveUp = moveDown = moveLeft = moveRight = False
    hero = Character(15, 10)
    enemy = Character(20, 20)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_BACKSPACE:
                    newGame = True
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_UP or event.key == K_k:
                    moveUp = True
                elif event.key == K_DOWN:
                    moveDown = True
                elif event.key == K_LEFT:
                    moveLeft = True
                elif event.key == K_RIGHT:
                    moveRight = True
              
            

        # move the player (if allowed)
        
        if moveUp and (hero.posx, hero.posy) != (20,21):
            hero.posy -= 1
        elif moveDown and (hero.posx, hero.posy) != (20,19):
            hero.posy += 1
        elif moveLeft and (hero.posx, hero.posy) != (21,20):
            hero.posx -= 1
        elif moveRight and (hero.posx, hero.posy) != (19,20):
            hero.posx += 1

    
        if moveUp and (hero.posx, hero.posy) == (20,21):
            hero.attack(enemy)
        elif moveDown and (hero.posx, hero.posy) == (20,19):
            hero.attack(enemy)
        elif moveLeft and (hero.posx, hero.posy) == (21,20):
            hero.attack(enemy)
        elif moveRight and (hero.posx, hero.posy) == (19,20):
            hero.attack(enemy)

        moveUp = moveDown = moveLeft = moveRight = False


        # display
        win.fill('.', region = (10, 5, 50, 25), fgcolor='silver', bgcolor='olive')
        win.putchar('@', hero.posx, hero.posy)
        win.putchar('v', enemy.posx, enemy.posy)
        win.write('Your health: ' + str(hero.health), 10, 0, fgcolor='white')
        win.write('Virus health: ' + str(enemy.health), 10, 1, fgcolor='white')
        win.write('Items:', 0, 5, fgcolor='white')
        win.update()
        pygame.display.update()
        

        if hero.health == 0:
            break

        if enemy.health == 0:
            break

        
        
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