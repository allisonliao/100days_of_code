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

        width, height = self.blob_img.get_size()

        if self.type == TYPE_AVATAR:
            x = (DISPLAY_WIDTH - width) // 2
            y = DISPLAY_HEIGHT - height
        elif self.type == TYPE_DROPPING_ENEMY:
            x = random.randint(0, DISPLAY_WIDTH - width)
            y = -height
        else:
            x = 0
            y = 0

        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, display):
        display.blit(self.blob_img, (self.rect.x, self.rect.y))

    def move_by(self, x_change, y_change):
        self.rect.x += x_change
        self.rect.y += y_change

        if self.type == TYPE_AVATAR:
            x_max = DISPLAY_WIDTH - self.rect.width
            if self.rect.x < 0:
                self.rect.x = 0
            elif self.rect.x > x_max:
                self.rect.x = x_max

    def is_dead(self):
        return self.rect.y >= DISPLAY_HEIGHT

    def is_touching(self, rect):
        return self.rect.colliderect(rect)


class Board:
    def __init__(self):
        self.display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()
        pygame.font.init()

        # create objects
        self.avatar = Thing(TYPE_AVATAR)
        self.enemies = []
        self.enemies.append(Thing(TYPE_DROPPING_ENEMY))

        self.game_exit = False

        self.game_score = 0

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
                if enemy.is_touching(self.avatar.rect):
                    quit()

            # draw
            self.draw()

            pygame.display.update()
            self.clock.tick(60)

            self.game_score += 1

            # things maintenance
            self.enemies = [thing for thing in self.enemies if not thing.is_dead()]

            if random.randint(0, 100) == 0:
                self.enemies.append(Thing(TYPE_DROPPING_ENEMY))

    def draw(self):
        self.display.fill(BLACK)
        self.avatar.draw(self.display)
        for enemy in self.enemies:
            enemy.draw(self.display)
        x_font = pygame.font.SysFont('Comic Sans MS', 30)
        text_surface = x_font.render('Score: ' + str(self.game_score), False, (0, 0, 255))
        self.display.blit(text_surface, (0, 0))

    def remove(self, thing):
        pass


def main():
    # Create board
    board = Board()

    # run game loop
    board.game_loop()


if __name__ == '__main__':
    main()
