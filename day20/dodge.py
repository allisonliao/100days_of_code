import pygame
import time
import random


TYPE_AVATAR = 1
TYPE_DROPPING_ENEMY = 2
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BLACK = (0, 0, 0)


class Thing:

    def __init__(self, t):
        self.type = t

        if self.type == TYPE_AVATAR:
            self.blob_img = pygame.image.load('blob2.png')
        elif self.type == TYPE_DROPPING_ENEMY:
            self.blob_img = pygame.image.load('blob_enemy.png')
            x = random.randint(50, 150)
            self.blob_img = pygame.transform.scale(self.blob_img, (x, x))

        self.width, self.height = self.blob_img.get_size()

        if self.type == TYPE_AVATAR:
            self.x = (DISPLAY_WIDTH - self.width) // 2
            self.y = DISPLAY_HEIGHT - self.height
        elif self.type == TYPE_DROPPING_ENEMY:
            self.x = random.randint(0, DISPLAY_WIDTH - self.width)
            self.y = -self.height

    def draw(self, display):
        display.blit(self.blob_img, (self.x, self.y))

    def move_by(self, x_change, y_change):
        self.x += x_change
        self.y += y_change

        if self.type == TYPE_AVATAR:
            x_max = DISPLAY_WIDTH - self.width
            if self.x < 0:
                self.x = 0
            elif self.x > x_max:
                self.x = x_max


class Board:
    def __init__(self):
        self.display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()

        # create objects
        self.avatar = Thing(TYPE_AVATAR)
        self.enemies = []
        self.enemies.append(Thing(TYPE_DROPPING_ENEMY))

        self.game_exit = False

    def game_loop(self):
        x_change = 0
        while not self.game_exit:
            # event handlers
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    elif event.key == pygame.K_RIGHT:
                        x_change = 5
                    # if event.key == pygame.K_p:
                    #     pause = True
                    #     paused()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

            # thing movements
            if x_change != 0:
                self.avatar.move_by(x_change, 0)

            for enemy in self.enemies:
                enemy.move_by(0, 5)

            # draw
            self.draw()

            pygame.display.update()
            self.clock.tick(60)

            # thing creation
            if random.randint(0, 100) == 0:
                self.enemies.append(Thing(TYPE_DROPPING_ENEMY))

    def draw(self):
        self.display.fill(BLACK)
        self.avatar.draw(self.display)
        for enemy in self.enemies:
            enemy.draw(self.display)

    def remove(self, thing):
        pass


def main():
    # Create board
    board = Board()

    # run game loop
    board.game_loop()


if __name__ == '__main__':
    main()
