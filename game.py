import pygame
import math
import random
from mushroom import Mushroom

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 600))
        self.clock = pygame.time.Clock()
        self.running = True

        # Load and scale background image
        self.background = pygame.image.load("background.png").convert()
        self.background = pygame.transform.scale(self.background, (self.background.get_width()*2.5, self.background.get_height()*2.5))
        self.bg_width = self.background.get_width()
        self.bg_tiles = math.ceil(self.screen.get_width() / self.bg_width)

        # Load and scale floor image
        self.floor = pygame.image.load("grass.jpeg").convert()
        self.floor = pygame.transform.scale(self.floor, (self.floor.get_width()*1.5, self.floor.get_height()*1.5)) 
        self.floor_width = self.floor.get_width()
        self.floor_tiles = math.ceil(self.screen.get_width() / self.floor_width)
        print(f"Tiles needed: {self.floor_tiles, self.bg_tiles}")

        # Scroll variables
        self.bg_scroll = 0
        self.floor_scroll = 0

        # Load and scale player image
        self.player = pygame.image.load("player.png").convert_alpha()
        self.player= pygame.transform.scale(self.player, (self.player.get_width() * 0.4, self.player.get_height() * 0.4))
        self.player.set_colorkey((255, 255, 255)) 

        # Player position
        self.player_pos = pygame.Vector2(self.screen.get_width()/2-100, self.screen.get_height() - 250)

        # Player jumping variables
        self.is_jumping = False
        self.jump_speed = 20
        self.gravity = 1
        self.jump_height = 20

        # Mushroom variables
        self.mushroom = Mushroom(self.screen)


    def run(self):
        while self.running:

            # Handle input
            keys = pygame.key.get_pressed()
            dt = 0.04
            if keys[pygame.K_LEFT]:
                self.bg_scroll -= 300 * dt
                self.floor_scroll -= 300 * dt
                self.mushroom.move(int(300 * dt), "left")
            if keys[pygame.K_RIGHT]:
                self.bg_scroll += 300 * dt
                self.floor_scroll += 300 * dt
                self.mushroom.move(int(300 * dt), "right")

            # Handle jumping
            if keys[pygame.K_SPACE] and not self.is_jumping:
                self.is_jumping = True
                print("space-bar pressed")
            if self.is_jumping:
                self.player_pos.y -= self.jump_speed
                self.jump_speed -= self.gravity
                if self.jump_speed < -self.jump_height:
                    print("jump complete")
                    self.is_jumping = False
                    self.jump_speed = self.jump_height
                    self.player_pos.y = 350
            
            # Loop the floor
            if self.floor_scroll <= -self.floor_width:
                self.floor_scroll += self.floor_width
            elif self.floor_scroll >= self.floor_width:
                self.floor_scroll -= self.floor_width
            elif self.floor_scroll < 0:
                self.floor_scroll += self.floor_width
            
            # Loop the background
            if self.bg_scroll < 0:
                self.bg_scroll += self.bg_width
            elif self.bg_scroll >= self.bg_width:
                self.bg_scroll -= self.bg_width
            elif self.bg_scroll <= -self.bg_width:
                self.bg_scroll += self.bg_width

            # Draw everything
            
            # Update background scrolling logic
            for i in range(0, self.bg_tiles + 1):
                x_position = (i * self.bg_width) - self.bg_scroll
                self.screen.blit(self.background, (x_position, 0)) 
            
            # Update floor scrolling logic
            for i in range(0, self.floor_tiles + 1):
                x_position = (i * self.floor_width) - self.floor_scroll
                self.screen.blit(self.floor, (x_position, 450))

            # Reset scroll to prevent overflow
            if abs(self.floor_scroll) > self.floor_width:
                self.floor_scroll %= self.floor_width

            # Prevent the player from going below the floor height
            if self.player_pos.y > 350: 
                self.player_pos.y = 350
                print("player too low, resetting position")
                self.is_jumping = False
                self.jump_speed = self.jump_height

            self.screen.blit(self.player, self.player_pos)
            self.mushroom.draw()


            pygame.display.flip()  # Update the display
            self.clock.tick(30)  # Limit to 60 frames per second

            for event in pygame.event.get():
                if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                    self.running = False

        pygame.quit()

Game().run()