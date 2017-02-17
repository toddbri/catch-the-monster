import pygame
import random
import time, math

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
F = 102
S = 115
Q = 113
ENTER = 13

class Goblins(object):
    def __init__(self):
        self.goblins = []
    def add_goblin(self,goblin):
        self.goblins.append(goblin)
    def remove_goblin(self,goblin):
        del self.goblins[goblins.index(goblin)]
    def render(self,screen):
        for goblin in self.goblins:
            goblin.render(screen)
    def move(self):
        for goblin in self.goblins:
            goblin.move()
    def collision(self,hero):
        for goblin in self.goblins:
            if hero.ff == True:
                if (math.sqrt((hero.x - goblin.x)**2 + (hero.y-goblin.y)**2) <66):
                    if (hero.x == goblin.x):
                        if goblin.y<hero.y:
                            goblin.y -=50
                        else:
                            goblin.y +=50
                    else:
                        m = (goblin.y-hero.y)/(goblin.x-hero.x)
                        if goblin.x>hero.x:
                            goblin.x +=int(50/math.sqrt(1+m**2))
                            goblin.y +=int(m*50/math.sqrt(1+m**2))
                        else:
                            goblin.x -=int(50/math.sqrt(1+m**2))
                            goblin.y +=int(m*50/math.sqrt(1+m**2))
            else:
                if (math.sqrt((hero.x - goblin.x)**2 + (hero.y-goblin.y)**2) <32):
                    return True
    def restart(self):
        for goblin in self.goblins:
            goblin.__init__()

class Monsters(object):
    def __init__(self):
        self.monsters = []
    def add_monster(self,monster):
        self.monsters.append(monster)
    def remove_monster(self,monster):
        del self.monster[self.monsters.index(monster)]
    def render(self,screen):
        for monster in self.monsters:
            monster.render(screen)
    def move(self):
        for monster in self.monsters:
            monster.move()
    def collision(self,hero):
        for monster in self.monsters:
            if monster.isalive()==True:
                if (math.sqrt((hero.x - monster.x)**2 + (hero.y-monster.y)**2) <32):
                    monster.dead()
                    del self.monsters[self.monsters.index(monster)]
        return len(self.monsters)
    def restart(self):
        for monster in self.monsters:
            monster.__init__()
class Character(object):
    def render(self, screen):
        if self.alive == True:
            screen.blit((self.image),(self.x, self.y))
    def dead(self):
        self.alive = False
    def isalive(self):
        return self.alive

class Goblin(Character):
    def __init__(self):
        self.width = 512
        self.time = time.time()-2
        self.height = 480
        self.speed = 1
        self.hidden = False
        self.alive = True
        self.x = int(100 * random.uniform(0.0,1.0)) + 400 * random.randint(0,1)
        self.y = int(100 * random.uniform(0.0,1.0)) + 400 * random.randint(0,1)
        self.image = pygame.image.load('goblin.png').convert_alpha()

    def move(self):
        if time.time() - self.time > 2:
            self.movement = random.randint(1,8)
            self.time = time.time()

        if self.movement == 1:
            self.x += self.speed
        if self.movement == 2:
            self.y += self.speed
        if self.movement == 3:
            self.x -= self.speed
        if self.movement == 4:
            self.y -= self.speed
        if self.movement == 5:
            self.y -= self.speed
            self.x -= self.speed
        if self.movement == 6:
            self.y -= self.speed
            self.x += self.speed
        if self.movement == 7:
            self.y += self.speed
            self.x += self.speed
        if self.movement == 8:
            self.y += self.speed
            self.x -= self.speed

        if self.x > self.width+16:
            self.x = -16
        if self.x < -16:
            self.x = self.width+16
        if self.y > self.height+16:
            self.y = -16
        if self.y < -16:
            self.y = self.height+16

class Hero(Character):
    def __init__(self):
        self.width = 512
        self.height = 480
        self.speed = 20
        self.ff = False
        self.ffcount = 3
        self.time = time.time()
        self.alive = True
        self.hidden = False
        self.x = self.width/2 -16
        self.y = self.height/2 -16
        self.image = pygame.image.load('hero.png').convert_alpha()
        self.forcefield = pygame.image.load('ff2.png').convert_alpha()
    def render(self, screen):
            screen.blit((self.image),(self.x, self.y))
            if self.ff == True:
                screen.blit((self.forcefield),(self.x-34,self.y-34))
                if time.time()-self.time > 3.5:
                    self.ff = False
    def forcefieldon(self):
        if self.ffcount > 0:
            self.ff = True
            self.ffcount -=1
            self.time = time.time()
    def move(self, event):
        if event == KEY_DOWN:
            self.y += self.speed
        if event == KEY_UP:
            self.y -= self.speed
        if event == KEY_RIGHT:
            self.x += self.speed
        if event == KEY_LEFT:
            self.x -= self.speed

        self.x = (self.x if self.x <= self.width-32 else self.width -32)
        self.y = (self.y if self.y <= self.height-32 else self.height-32)
        self.x = (0 if self.x < 0 else self.x)
        self.y = (0 if self.y < 0 else self.y)


class Monster(Character):
    def __init__(self):
        self.alive = True
        self.hidden = False
        self.width = 512
        self.height = 480
        self.time = time.time() -2
        self.speed = 2
        self.movement = 0
        self.x = int(100 * random.uniform(0.0,1.0)) + 400 * random.randint(0,1)
        self.y = int(100 * random.uniform(0.0,1.0)) + 400 * random.randint(0,1)
        self.image = pygame.image.load('monster.png').convert_alpha()

    def move(self):
        if time.time() - self.time > 2:
            self.movement = random.randint(1,8)
            self.time = time.time()

        if self.movement == 1:
            self.x += self.speed
        if self.movement == 2:
            self.y += self.speed
        if self.movement == 3:
            self.x -= self.speed
        if self.movement == 4:
            self.y -= self.speed
        if self.movement == 5:
            self.y -= self.speed
            self.x -= self.speed
        if self.movement == 6:
            self.y -= self.speed
            self.x += self.speed
        if self.movement == 7:
            self.y += self.speed
            self.x += self.speed
        if self.movement == 8:
            self.y += self.speed
            self.x -= self.speed

        if self.x > self.width+16:
            self.x = -16
        if self.x < -16:
            self.x = self.width+16
        if self.y > self.height+16:
            self.y = -16
        if self.y < -16:
            self.y = self.height+16


def main():
    pygame.init()
    sounds = True
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    sound_winner = pygame.mixer.Sound('win.wav')
    sound_goblin = pygame.mixer.Sound('lose.wav')
    screen = pygame.display.set_mode((width, height))
    hero = Hero()
    background = pygame.image.load('background.png').convert_alpha()


    pygame.display.set_caption('Capture the Monster')
    clock = pygame.time.Clock()
    new_game = True
    while new_game:
        stop_game = False
        screen.fill(blue_color)
        screen.blit(background, (0, 0))
        font = pygame.font.Font(None, 45)
        text = font.render('Level(1-9)?', True, (51, 82, 195))
        screen.blit(text, (175, 175))
        pygame.display.update()
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    print event.key
                    if event.key in range(49,58):
                        pause = False
                        level = event.key -48
                        print level
                if event.type == pygame.QUIT:
                    pause = False
                    new_game = False
                    stop_game = True
        goblins = Goblins()
        monsters = Monsters()
        hero.__init__()
        for i in range(level):
            goblins.add_goblin(Goblin())
        for i in range(level):
            monsters.add_monster(Monster())
        # Game initialization


        while not stop_game:
            monsters.move()
            goblins.move()

        # Event handling
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == Q:
                        stop_game = True
                        new_game = False
                    if event.key == S:
                        sounds = not sounds
                    if event.key == F:
                        hero.forcefieldon()
                    if event.key in [273,274,275,276]:
                        hero.move(event.key)
                if event.type == pygame.QUIT:
                    stop_game = True
            # Game logic

            # Draw background
            screen.fill(blue_color)
            screen.blit(background, (0, 0))

            goblins.render(screen)
            monsters.render(screen)
            hero.render(screen)
            # Game display

            pygame.display.update()
            if monsters.collision(hero) == 0:
                if sounds:
                    sound_winner.play()
                font = pygame.font.Font(None, 45)
                text = font.render('You Win!!', True, (51, 82, 195))
                screen.blit(text, (200, 175))
                text = font.render('Press ENTER to play again.', True, (255, 0, 0))
                screen.blit(text, (65, 230))
                pygame.display.update()
                onward = True
                while onward:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            print event.key
                            if event.key == Q:
                                onward = False
                                stop_game = True
                                new_game = False
                            elif event.key == ENTER:
                                stop_game = True
                                onward = False
                                new_game = True
                        if event.type == pygame.QUIT:
                            stop_game = True
                            onward = False
                            new_game = False
            else:
                if goblins.collision(hero):
                    if sounds:
                        sound_goblin.play()
                    font = pygame.font.Font(None, 45)
                    text = font.render('You Lose!!', True, (51, 82, 195))
                    screen.blit(text, (200, 175))
                    text = font.render('Press ENTER to play again.', True, (255, 0, 0))
                    screen.blit(text, (65, 230))
                    pygame.display.update()
                    onward = True
                    while onward:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                print event.key
                                if event.key == Q:
                                    onward = False
                                    stop_game = True
                                    new_game = False
                                elif event.key == ENTER:
                                    onward = False
                                    new_game = True
                                    stop_game = True
                            if event.type == pygame.QUIT:
                                stop_game = True
                                new_game = False
                                onward = False

            clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
