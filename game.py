import pygcurse, pygame, sys, time, random
from pygame.locals import *

FPS = 30
BLACK = (0,0,0)
RED = (255,0,0)

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
    moveLeft = moveRight = moveUp = moveDown = False
    lastmovetime = sys.maxsize
    mainClock = pygame.time.Clock()

    hero = Character(5, 5)
    enemy = Character(10, 10)
    

    while True:
        # handle input
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
                    moveDown = False
                elif event.key == K_DOWN:
                    moveDown = True
                    moveUp = False
                elif event.key == K_LEFT:
                    moveLeft = True
                    moveRight = False
                elif event.key == K_RIGHT:
                    moveRight = True
                    moveLeft = False
                lastmovetime = time.time() - 1

            elif event.type == KEYUP:
                if event.key == K_UP or event.key == K_k:
                    moveUp = False
                elif event.key == K_DOWN:
                    moveDown = False
                elif event.key == K_LEFT:
                    moveLeft = False
                elif event.key == K_RIGHT:
                    moveRight = False

        # move the player (if allowed)
        if time.time() - 0.1 > lastmovetime:
            if moveUp and (hero.posx, hero.posy) != (10,11):
                hero.posy -= 1
            elif moveDown and (hero.posx, hero.posy) != (10,9):
                hero.posy += 1
            elif moveLeft and (hero.posx, hero.posy) != (11,10):
                hero.posx -= 1
            elif moveRight and (hero.posx, hero.posy) != (9,10):
                hero.posx += 1

        if time.time() - 0.1 > lastmovetime:
            if moveUp and (hero.posx, hero.posy) == (10,11):
                hero.attack(enemy)
            elif moveDown and (hero.posx, hero.posy) == (10,9):
                hero.attack(enemy)
            elif moveLeft and (hero.posx, hero.posy) == (11,10):
                hero.attack(enemy)
            elif moveRight and (hero.posx, hero.posy) == (9,10):
                hero.attack(enemy)

            lastmovetime = time.time()
            

        # display
        win.fill('.', region = (10, 5, 50, 25), fgcolor='silver', bgcolor='olive')
        win.putchar('@', hero.posx, hero.posy)
        win.putchar('v', enemy.posx, enemy.posy)
        win.pygprint('Your health: ', hero.health)
        win.pygprint('Virus health: ', enemy.health)

        if hero.health == 0:
        	break

        if enemy.health == 0:
        	break

        win.update()
        pygame.display.update()
        mainClock.tick(FPS)

	if hero.health == 0:
		win.pygprint('You lose.', x=0, y=0)
		pygcurse.waitforkeypress()

	if enemy.health == 0:
		win.pygprint('You win!', x=0, y=0)
		pygcurse.waitforkeypress()
  
    	


if __name__ == '__main__':
    main()